import base64
import fitz

class FileService:
    def convert_pdf_to_images(self, pdf_file):
        """Convert PDF to list of base64 strings"""
        pdf_bytes = pdf_file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        images = []
        
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))
            img_bytes = pix.tobytes("png")
            base64_image = base64.b64encode(img_bytes).decode('utf-8')
            images.append(base64_image)
        
        return images
    
    def process_uploaded_file(self, uploaded_file, vision_service):
        """Process uploaded file and return analysis"""
        if uploaded_file.type == "application/pdf":
            images_base64 = self.convert_pdf_to_images(uploaded_file)
            all_text = []
            
            for idx, base64_image in enumerate(images_base64):
                text_content = vision_service.analyze_image(base64_image)
                all_text.append(f"## Page {idx + 1}\n\n{text_content}\n\n")
            
            return "\n".join(all_text)
        else:
            image_bytes = uploaded_file.read()
            base64_image = base64.b64encode(image_bytes).decode('utf-8')
            return vision_service.analyze_image(base64_image)
