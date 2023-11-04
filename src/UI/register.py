import gradio as gr

def register():
    #logica enviar datos a los contratos
    return "Usuario registrado"

with gr.Blocks() as interface:
    name = gr.Textbox(label="Nombres")
    surname = gr.Textbox(label="Apellidos")
    id = gr.Textbox(label="Cedula")
    output = gr.Textbox(None)
    greet_btn = gr.Button("Registrarse")
    greet_btn.click(fn=register,outputs=output, api_name="register")

# Launch the Gradio interface.
if __name__ == "__main__":
    interface.launch(share=True)

