import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pikepdf as pike
import graphviz

img = Image.open('logo.jpg')
st.set_page_config(page_title='PDF TOOLKIT', page_icon=img)

########## Functions ##########
def Encrypte_PDF(file,my_pass):
    old_file = pike.Pdf.open(file)
    no_extr = pike.Permissions(extract=False)
    Encrypted_file = old_file.save('Encrypted.pdf', encryption=pike.Encryption(user=my_pass,owner='admin',allow=no_extr))
    return Encrypted_file

def Decryptre_PDF(file, old_pass):
    decryptred_file = pike.open(file, password=old_pass)
    Decryptred_file = decryptred_file.save('Decrypted.pdf')
    return Decryptred_file

def Merger_PDF(files):
      merger_pdf = pike.Pdf.new()
      for pdf in files:
           with pike.open(pdf) as PDF:
              merger_pdf.pages.extend(PDF.pages)
      return merger_pdf.save('Merged.pdf') 



with st.sidebar:
    selected = option_menu('Menu', ['Home', 'Upload PDF', 'AboutUS'], 
        icons=['house', 'cloud-upload', 'chat'], menu_icon='menu', default_index=0)

if selected == 'Home':
    st.subheader("PDF Toolkit :lock: ", divider='rainbow')

    st.subheader('Which Moduel Use For This Project')
    st.code(f"""
    import streamlit as st
    from streamlit_option_menu import option_menu
    from PIL import Image
    import pikepdf as pike
    import home as Home
    import aboutus as About
    """)
    
    st.subheader("How PDF Uploader Work?")
    graph = graphviz.Digraph()
    graph.edge('Upload PDF', 'Not Upload')
    graph.edge('Not Upload', 'Upload PDF')
    graph.edge('Upload PDF', 'Uploaded')
    graph.edge('Uploaded', 'Select Option')
    graph.edge('Select Option', 'DE-Encrypte PDF')
    graph.edge('DE-Encrypte PDF', 'Encrypte')
    graph.edge('Encrypte', 'Dowload PDF')
    graph.edge('Decrypte', 'Dowload PDF')
    graph.edge('DE-Encrypte PDF', 'Decrypte')
    graph.edge('Select Option', 'Merge PDF')
    graph.edge('Merge PDF', 'Download PDF')
    st.graphviz_chart(graph)

elif  selected=='Upload PDF':
        option = st.selectbox(
    "What Do You Do?",
    ('De-Encrypt', 'Merger'))
        uploaded_file = st.file_uploader("Choose your .pdf file", type = 'pdf', accept_multiple_files = False if option == 'De-Encrypt' else True)

        if option == 'De-Encrypt':
              genre = st.radio(
            "Select Your Option",
            ['Encrypt File', 'Decrypt File'],
            index=None,
        )
              if genre == 'Encrypt File':
                  new_pass = st.text_input("SET PDF NEW PASSWORD : ", 'Password')
                  if st.button('Next', disabled=False, type = 'primary'):
                      my_pass = new_pass 
                      st.write("Your Password is : ", new_pass)
                  try:
                      Encrypte_PDF(uploaded_file,my_pass)
                      with open('Encrypted.pdf', 'rb') as pdf_file:
                          PDFbyte = pdf_file.read()
                      st.download_button(label='Download_pdf', data= PDFbyte, file_name='Encrypted_pdf.pdf', mime='application/octet-strem')
                  except  Exception as e:
                      st.error("File Not Uploaded !!!")
      
              elif genre == 'Decrypt File':
                  old_pass = st.text_input("ENTER PDF OLD PASSWORD : ",'Password')
                  if st.button('Next', disabled=False, type = 'primary'):
                      my_pass = old_pass
                      st.write("Your Password is : ", old_pass)
                  try:
                      Decryptre_PDF(uploaded_file,my_pass)
                      with open('Decrypted.pdf', 'rb') as pdf_file:
                          PDFbyte = pdf_file.read()
                      st.download_button(label='Download_pdf', data= PDFbyte, file_name='Decrypted_pdf.pdf', mime='application/octet-strem')
                  except  Exception as e:
                      st.error("File Not Uploaded !!!")

        elif option == 'Merger':
              st.text("*** NOTE : Please All PDF File Select In One Time Like (1.PDF,2.PDF,3.PDF) ***")
              Merger_PDF(uploaded_file)
              if st.button('Merge', disabled=False, type = 'primary'):
                      with open('Merged.pdf', 'rb') as pdf_file:
                          PDFbyte = pdf_file.read()
                      st.download_button(label='Download_pdf', data= PDFbyte, file_name='Merged_pdf.pdf', mime='application/octet-strem')

else:
    st.text("This Pdf Toolkit Create By Mohit Nandaniya in 2024")
    st.text("Thanks For Use it")
    st.text("Email : nandaniyamohit02@gmail.com")
    st.text("instagram : @Devlp_Mohit")
    st.text("Website : Devlp_Mohit.io")