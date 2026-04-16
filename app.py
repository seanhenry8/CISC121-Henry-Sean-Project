import gradio as gr
import copy
import time

def calculate_score(gpa: float, vol_hours: int, essay_score: int) -> float: # calulates a one number score out of 100 based on the inputs
    weight_gpa = (gpa / 4.0) * 40    
    capped_vol = min(vol_hours, 100)
    weight_vol = (capped_vol / 100.0) * 20
    weight_essay = (essay_score / 100.0) * 40
    return round(weight_gpa + weight_vol + weight_essay, 2)

def generate_plot(applicants, highlighted_indices=None, success=False): # creates bars for visuals
    html = "<div style='display: flex; align-items: flex-end; justify-content: space-around; height: 300px; background: #111; padding: 20px; border-radius: 10px;'>"
    
    for i, app in enumerate(applicants):
        score = app['final_score']
        # determine bar color based on state
        color = "#eab308"  # default yellow
        if success:
            color = "#22c55e"  # final success green
        elif highlighted_indices and i in highlighted_indices:
            color = "#22c55e"  # active merge green
            
        height = max((score / 100) * 250, 10)
        
        html += f"""
        <div style="display: flex; flex-direction: column; align-items: center; width: 100%;">
            <div style="background-color: {color}; height: {height}px; width: 80%; border-radius: 4px 4px 0 0; transition: all 0.3s ease;"></div>
            <span style="color: white; font-size: 10px; margin-top: 5px; font-weight: bold;">{score}</span>
            <span style="color: #888; font-size: 9px;">{app['name']}</span>
        </div>
        """
    html += "</div>"
    return html

def merge_sort_animated(applicants):

    arr = copy.deepcopy(applicants)
    
    def sort_recursive(start, end): # base case of list length 1
        if end - start <= 1:
            return
        
        mid = (start + end) // 2 #split list in half
        yield from sort_recursive(start, mid)
        yield from sort_recursive(mid, end)
        
        # Merge process
        left = arr[start:mid]
        right = arr[mid:end]
        
        i = j = 0
        k = start
        
        while i < len(left) and j < len(right):
            # Compare and highlight the decision
            if left[i]['final_score'] >= right[j]['final_score']:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            
            yield arr, [k], f"Comparing and placing {arr[k]['name']}"
            k += 1

        while i < len(left):
            arr[k] = left[i]
            yield arr, [k], f"Placing remaining: {arr[k]['name']}"
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            yield arr, [k], f"Placing remaining: {arr[k]['name']}"
            j += 1
            k += 1

    yield from sort_recursive(0, len(arr))
    yield arr, [], "Sorting Complete!"

def run_app(data_input):
    # input: "Name, GPA, Vol, Essay" per line
    try:
        applicants = []
        lines = data_input.strip().split("\n")
        for line in lines:
            parts = [p.strip() for p in line.split(",")]
            name, gpa, vol, essay = parts[0], float(parts[1]), int(parts[2]), int(parts[3])
            score = calculate_score(gpa, vol, essay)
            applicants.append({"name": name, "final_score": score})
    except Exception as e:
        yield gr.update(value="Error: Please use format 'Name, GPA, Vol, Essay' per line."), "", "" # edge case
        return

    yield generate_plot(applicants), "Starting Sort...", ""

    # animation Loop
    final_list = []
    for current_state, highlighted, message in merge_sort_animated(applicants):
        time.sleep(1) # animation speed
        final_list = current_state
        yield generate_plot(current_state, highlighted), message, ""

    # success State
    time.sleep(0.3)
    results_text = "\n".join([f"{i+1}. {a['name']} ({a['final_score']})" for i, a in enumerate(final_list)])
    yield generate_plot(final_list, success=True), "Task Successful!", results_text

# gui layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Visual Merge Sort: Applicant Ranking")
    gr.Markdown("Enter applicant data below (one per line). Format: `Name, GPA, VolunteerHours, EssayScore`")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_data = gr.Textbox(
                label="Applicant Data", 
                lines=8, 
                value="Alice, 3.8, 50, 90\nBob, 3.2, 100, 75\nCharlie, 3.9, 10, 95\nDave, 2.5, 120, 60\nEve, 4.0, 20, 85"
            )
            sort_btn = gr.Button("Start Ranking", variant="primary")
            status_msg = gr.Markdown("### Status: Waiting")
            
        with gr.Column(scale=2):
            plot_output = gr.HTML(label="Visualization")
            results_output = gr.Textbox(label="Final Ranking", interactive=False)

    sort_btn.click(
        fn=run_app, 
        inputs=[input_data], 
        outputs=[plot_output, status_msg, results_output]
    )

if __name__ == "__main__":
    demo.launch()
