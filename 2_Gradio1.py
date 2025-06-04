import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Hello")
    gr.Markdown("## 여기는 제목을 입력합니다.")
    gr.Markdown("- 첫 번째 아이템\n- 두 번째 아이템\n- 세 번째 아이템")


demo.launch()