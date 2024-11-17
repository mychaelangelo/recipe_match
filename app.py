import streamlit as st
from dotenv import load_dotenv
import os
from services.vision_service import VisionService
from services.file_service import FileService
from utils.error_handler import handle_processing_error
from utils.prompt_loader import load_prompt
from ui.components import (
    render_title,
    render_api_key_input,
    render_input_method_selector,
    render_results
)

def initialize_services():
    """Initialize services with API key"""
    load_dotenv()
    
    # Simplified API key retrieval chain
    api_key = os.getenv('OPENAI_API_KEY') or st.session_state.get('api_key')
    
    if not api_key:
        api_key = st.text_input("Enter your OpenAI API Key:", type="password")
        if api_key:
            st.session_state['api_key'] = api_key
        else:
            st.warning("Please enter your OpenAI API key to continue.")
            return None
    
    return VisionService(api_key), FileService()

def handle_processing(vision_service, input_data, process_func):
    """Generic handler for processing inputs"""
    if input_data and st.button("Process Image"):
        with st.status("Processing...") as status:
            try:
                if st.button("Cancel", key="cancel_button"):
                    st.stop()
                    status.update(label="Cancelled", state="error")
                    return

                result = process_func(input_data)
                status.update(label="Complete!", state="complete")
                
            except Exception as e:
                status.update(label="Error occurred", state="error")
                handle_processing_error(e)
                return
            
        # Display results
        render_results(result)
        
        # Add reset button after processing
        if st.button("Start New Analysis"):
            st.session_state.clear()
            st.experimental_rerun()

def handle_camera_input(vision_service):
    """Handle camera input processing"""
    camera_input = st.camera_input("Take a picture")
    
    # Add preview of captured image
    if camera_input:
        st.image(camera_input, caption="Preview of captured image")
        
    handle_processing(vision_service, camera_input, 
                     vision_service.process_camera_input)

def handle_file_upload(vision_service, file_service):
    """Handle file upload processing"""
    uploaded_file = st.file_uploader(
        "Upload a PDF or image file (supported formats: PDF, PNG, JPEG, JPG)", 
        type=["pdf", "png", "jpg", "jpeg"]
    )
    
    if uploaded_file:
        handle_processing(vision_service, uploaded_file,
                         lambda f: file_service.process_uploaded_file(f, vision_service))

def main():
    render_title()
    
    services = initialize_services()
    if not services:
        return
    
    vision_service, file_service = services
    input_method = render_input_method_selector()
    
    if input_method == "Take Picture":
        handle_camera_input(vision_service)
    else:
        handle_file_upload(vision_service, file_service)

if __name__ == "__main__":
    main()