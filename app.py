import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables and configure API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Page configuration with custom theme
st.set_page_config(
    page_title="Pixel Whisperer: Sarcasm Meets AI for Photo PhD",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for unique styling
st.markdown("""
    <style>
    body {
        background-color: #1A1A2E;
        color: #EAEAEA;
    }
    .main {
        padding: 3rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3rem;
        background: linear-gradient(90deg, #FF416C, #FF4B2B);
        color: white;
        font-size: 16px;
        font-weight: bold;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #FF4B2B, #FF416C);
    }
    .uploadedImage {
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(255, 100, 100, 0.2);
    }
    .stTextArea>div>div>textarea {
        border-radius: 15px;
        padding: 1rem;
        background-color: #333;
        color: #EAEAEA;
    }
    .analysis-box {
        background-color: #222;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    raise FileNotFoundError("No file uploaded")

# Sidebar with snarky content
with st.sidebar:
    st.title("🖼️ Pixel Whisperer")
    st.markdown("## \"Where AI Deciphers Your Pixels Better Than You Ever Could!\"")
    st.markdown("---")
    st.markdown("""
        🤖 **About the Project**  
        Welcome to *Pixel Whisperer*, where sarcasm meets the brilliance of Google's 
        **Gemini AI** to turn your simple images into pure academic research!  
        
        **Features**:  
        - Detect sarcasm in your photos (just kidding, or are we?)  
        - Lightning-fast analysis that'll blow your pixels away  
        - Insights so deep, you'll feel like you have a PhD in photography  
    """)
    st.markdown("---")
    st.caption("AI Intelligence + Human Humor = Pixel Whisperer")

# Main content area
st.title("📸 Pixel Whisperer Studio")
st.subheader("“Making your image analysis extra... *fancy*! 🎩”")

# Two-column layout for enhanced interactivity
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Upload your masterpiece below:")
    input_prompt = st.text_area(
        "Enter your sarcastic query (or a serious one if you're boring):",
        placeholder="E.g., What hidden secrets lie in this JPEG file?",
        height=120
    )
    uploaded_file = st.file_uploader(
        "Upload Your Image (JPEG/PNG preferred for maximum snark):",
        type=["jpg", "jpeg", "png"],
        help="We promise not to judge your photography skills."
    )

with col2:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(
            image, 
            caption="Your image in all its pixelated glory 🖼️", 
            use_column_width=True, 
            clamp=True, 
            output_format="PNG"
        )
    else:
        st.info("👆 Upload something, we dare you!")

# Analyze button and results
if st.button("✨ Whisper to Gemini AI"):
    if not input_prompt.strip():
        st.error("⚠️ Enter a query, or Gemini will ignore you.")
    elif not uploaded_file:
        st.error("⚠️ We need an image too. Obviously.")
    else:
        with st.spinner("🤖 Whispering to Gemini AI..."):
            try:
                image_data = input_image_setup(uploaded_file)
                detailed_prompt = """
                You are the world's snarkiest yet most brilliant image analysis expert. 
                Analyze the uploaded image and provide outrageously detailed, useful, 
                and perhaps slightly sarcastic insights based on the user's query.
                """
                response = get_gemini_response(detailed_prompt, image_data, input_prompt)
                
                st.success("🎉 Analysis Complete! Here's what Gemini whispered:")
                st.markdown("### 📊 Deep Analysis Results")
                st.markdown(f"""
                    <div class='analysis-box'>
                        {response}
                    </div>
                """, unsafe_allow_html=True)

                # Option to download the analysis
                st.download_button(
                    label="📥 Download Results (Because Genius Deserves to Be Saved)",
                    data=response,
                    file_name="pixel_whisperer_analysis.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"🚫 Oops! Something went wrong: {str(e)}")
                st.info("💡 Pro Tip: Refresh and try again!")

# Footer with sarcastic closing
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Created with 🧠 + 😂 by a sarcastic AI enthusiast.</p>
        <p>“If you don’t upload an image, we won’t upload our insights!”</p>
    </div>
    """,
    unsafe_allow_html=True
)


# import streamlit as st
# from dotenv import load_dotenv
# import os
# from PIL import Image
# import google.generativeai as genai

# # Load environment variables and configure API
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Page configuration with custom theme
# st.set_page_config(
#     page_title="Gemini Vision Pro",
#     page_icon="🔮",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS
# st.markdown("""
#     <style>
#     .main {
#         padding: 2rem;
#     }
#     .stButton>button {
#         width: 100%;
#         border-radius: 10px;
#         height: 3rem;
#         background-color: #FF4B4B;
#         color: white;
#         font-weight: bold;
#     }
#     .uploadedImage {
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#     }
#     .stTextArea>div>div>textarea {
#         border-radius: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# def get_gemini_response(input, image, prompt):
#     model = genai.GenerativeModel("gemini-2.0-flash-exp")
#     response = model.generate_content([input, image[0], prompt])
#     return response.text

# def input_image_setup(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()
#         image_parts = [{
#             "mime_type": uploaded_file.type,
#             "data": bytes_data
#         }]
#         return image_parts
#     raise FileNotFoundError("No file uploaded")

# # Sidebar with enhanced styling
# with st.sidebar:
#     st.title("🔮 Gemini Vision Pro")
#     st.markdown("---")
#     st.subheader("About")
#     st.markdown("""
#         Transform your images into insights with Gemini Vision Pro - powered by Google's 
#         advanced gemini-2.0-flash-exp model for lightning-fast image analysis.
        
#         **Features:**
#         - Advanced OCR capabilities
#         - Multi-format support
#         - Real-time analysis
#         - High accuracy results
#     """)
#     st.markdown("---")
#     st.caption("Powered by Gemini AI 2.0")

# # Main content area with two columns
# col1, col2 = st.columns([3, 2])

# with col1:
#     st.title("📸 Image Analysis Studio")
#     st.markdown("Upload your image and let Gemini AI reveal the insights within.")
    
#     input_prompt = st.text_area(
#         "What would you like to know about the image?",
#         placeholder="E.g., Extract all text and analyze the content in detail...",
#         height=100
#     )
    
#     uploaded_file = st.file_uploader(
#         "Upload Image (JPEG/PNG)",
#         type=["jpg", "jpeg", "png"],
#         help="Drag and drop or click to upload"
#     )

# with col2:
#     st.markdown("<br>" * 4, unsafe_allow_html=True)  # Add some spacing
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="Preview", use_column_width=True, clamp=True)
#     else:
#         st.info("👆 Upload an image to get started")

# # Analysis section
# if st.button("🔍 Analyze with Gemini AI", key="analyze"):
#     if not input_prompt.strip():
#         st.error("⚠️ Please enter a query first")
#     elif not uploaded_file:
#         st.error("⚠️ Please upload an image to analyze")
#     else:
#         with st.spinner("🤖 Gemini AI is analyzing your image..."):
#             try:
#                 image_data = input_image_setup(uploaded_file)
#                 detailed_prompt = """
#                 You are an advanced image analysis expert using the Gemini AI system.
#                 Analyze the provided image thoroughly and provide detailed insights
#                 based on the user's query. Include relevant details and maintain
#                 a professional tone in your response.
#                 """
#                 response = get_gemini_response(detailed_prompt, image_data, input_prompt)
                
#                 st.success("✨ Analysis Complete!")
#                 st.markdown("### 📊 Analysis Results")
#                 st.markdown(response)
                
#                 # Add option to download results
#                 st.download_button(
#                     label="📥 Download Analysis",
#                     data=response,
#                     file_name="gemini_analysis.txt",
#                     mime="text/plain"
#                 )
                
#             except Exception as e:
#                 st.error(f"🚫 An error occurred: {str(e)}")
#                 st.info("💡 Tip: Try uploading a different image or refreshing the page")

# # Footer
# st.markdown("---")
# st.markdown(
#     """
#     <div style='text-align: center'>
#         <p>Created with ❤️ using Streamlit and Gemini AI</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )