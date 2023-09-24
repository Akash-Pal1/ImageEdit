import cv2 as cv
import streamlit as st
import numpy as np
import all_functions as all
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Image Editor",
)

st.title("A Image Processing Webapp")

with st.sidebar:
    st.title("What can we do here?")
    page = st.radio(
        "Choose what you want to do here",
        ["**Apply filters** ", "**Flip Images**", "**Blur Images**"],
        captions=['Apply filters to your photos', "Flip Images ", "Blur Images to the intensity you want"]
    )


def apply_filter_sec():
    editor = all.Editor()
    st.title("Apply Filters to Images")
    st.markdown(f"**Apply your favourite filter to your images. The filter available are listed in the form of button in the below.**")
    filter = st.radio("Part 1",['Sepia','Canny','Inverse','GrayScale','HDR','Cartoonify','Winter','Summer','Oil Paint', 'Sharpen'],horizontal=True,label_visibility='hidden')


    original, filtered = st.columns(2)
    img = Image.open("coffee.jpg")
    img = np.array(img)
    if filter == 'Sepia':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.sepia(img))

    if filter == "Canny":
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.canny_edge(img))

    if filter == 'Inverse':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.get_inverse(img))

    if filter == 'GrayScale':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.changeToGrayScale(img))

    if filter == 'HDR':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.get_hdr(img))

    if filter == 'Cartoonify':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.cartoonify(img))

    if filter == 'Winter':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.winter_effect(img))

    if filter == 'Summer':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.summer_effect(img))

    if filter == 'Oil Paint':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.oilpainting(img))

    if filter == 'Sharpen':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            st.image(editor.sharpen(img))
    st.markdown("**Upload your file here in format of JPG, PNG, and JPEG**")
    file = st.file_uploader(label="FIle upload",type=['jpg', 'png','jpeg'], label_visibility="hidden")

    if file is None:
        st.info("No file is yet uploaded. Upload your file to see results")

    if file is not None:
        img_file = Image.open(file)
        img_file = np.array(img_file, dtype=np.uint8)
        original, filtered = st.columns(2)
        if filter == 'Sepia':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.sepia(img_file)
                st.image(img_c)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == "Canny":
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.canny_edge(img_file)
                st.image(img_c)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'Inverse':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.get_inverse(img_file)
                st.image(img_c)

                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'GrayScale':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.changeToGrayScale(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'HDR':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.get_hdr(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'Cartoonify':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.cartoonify(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'Winter':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.winter_effect(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'Summer':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.summer_effect(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'Oil Paint':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.oilpainting(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        if filter == 'Sharpen':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.sharpen(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)


        st.markdown("**Download your image by clicking the below button**")
        with open(temp_file_path, "rb") as file:
            btn = st.download_button(
            label="Download image",
            data=file.read(),  # Read the binary data from the file
            file_name="flitered.png",
            mime="image/png"
            )      


def flip_func():
    editor = all.Editor()

    st.title("Flip Your Images")
    st.markdown("**Flip Your Images as per your choice**")

    flipping = st.radio("Flipper",
                        ["**Flip Horizontally**","**Flip Vertically**", "**Flip Both**"], horizontal=True, label_visibility='hidden'
    )

    original, filtered = st.columns(2)
    img = Image.open("coffee.jpg")
    img = np.array(img)
    if flipping == '**Flip Horizontally**':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            img_c = editor.flip_horiz(img)
            st.image(img_c)
    if flipping == '**Flip Vertically**':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            img_c = editor.flip_verti(img)
            st.image(img_c)
    if flipping == '**Flip Both**':
        with original:
            st.title("Original")
            st.image(img)
        with filtered:
            st.title("With filter")
            img_c = editor.flip_both(img)
            st.image(img_c)
    
    st.markdown("**Upload your file here in format of JPG, PNG, and JPEG**")
    file = st.file_uploader(label="FIle upload",type=['jpg', 'png','jpeg'], label_visibility="hidden")

    if file is None:
        st.info("No file is yet uploaded. Upload your file to see results")

    if file is not None:
        img_file = Image.open(file)
        img_file = np.array(img_file, dtype=np.uint8)
        original, filtered = st.columns(2)

        if flipping == '**Flip Horizontally**':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.flip_horiz(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)
        if flipping == '**Flip Vertically**':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.flip_verti(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)
        if flipping == '**Flip Both**':
            with original:
                st.title("Original")
                st.image(img_file)
            with filtered:
                st.title("With filter")
                img_c = editor.flip_both(img_file)
                st.image(img_c)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file_path = temp_file.name
                    Image.fromarray(img_c).save(temp_file_path)

        



        st.markdown("**Download your image by clicking the below button**")
        with open(temp_file_path, "rb") as file:
            btn = st.download_button(
            label="Download image",
            data=file.read(),  # Read the binary data from the file
            file_name="flip.png",
            mime="image/png"
            )

def blur_sec():
    editor = all.Editor()
    st.title("Blur Your Images")
    st.markdown("**Blur Your Images as per your choice with your Chosen Intensity**")

    i =st.slider("Choose your Intensity", min_value=1, max_value=15, step=2)
    st.markdown("**How you image will look.**")
    original, filtered = st.columns(2)
    img = Image.open("coffee.jpg")
    img = np.array(img)
    with original:
        st.title("Original")
        st.image(img)
    with filtered:
        st.title("Blurred")
        img_c = editor.bluring(img,i)
        st.image(img_c)

    st.markdown("**Upload your file here in format of JPG, PNG, and JPEG**")
    file = st.file_uploader(label="FIle upload",type=['jpg', 'png','jpeg'], label_visibility="hidden")
    if file is None:
        st.info("No file is yet uploaded. Upload your file to see results")

    if file is not None:
        img_file = Image.open(file)
        img_file = np.array(img_file, dtype=np.uint8)
        original, filtered = st.columns(2)
        with original:
            st.title("Original")
            st.image(img_file)
        with filtered:
            st.title("Blurred")
            img_c = editor.bluring(img_file,i)
            st.image(img_c)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file_path = temp_file.name
                Image.fromarray(img_c).save(temp_file_path)

        st.markdown("**Download your image by clicking the below button**")
        with open(temp_file_path, "rb") as file:
            btn = st.download_button(
            label="Download image",
            data=file.read(),  # Read the binary data from the file
            file_name="blur.png",
            mime="image/png"
            )
    

    



if page == "**Apply filters** ":
    apply_filter_sec()
if page == "**Flip Images**":
    flip_func()
if page == "**Blur Images**":
    blur_sec()



    

















# file = None
# #file = st.file_uploader("Choose a file", type=['jpg','png','jpeg'])
# #file = st.camera_input("TAke a picture")

# editor = all.Editor()
# if file is not None:
#     file = Image.open(file)
#     file = np.array(file)
#     st.image(file)
#     imggray = editor.changeToGrayScale(file)
#     st.image(imggray)

#     imgblur = editor.bluring(file)
#     st.image(imgblur)

#     img_canny = editor.canny(file)
#     st.image(img_canny)

#     #img_crop = editor.crop(file, 400, 600,550, 750)
#     #st.image(img_crop)

#     img_hori_flip = editor.flip_horiz(file)
#     img_vert_flip = editor.flip_verti(file)
#     img_both_fiip = editor.flip_both(file)

#     st.image(img_hori_flip)
#     st.image(img_vert_flip)
#     st.image(img_both_fiip)
#     st.image(editor.cartoonify(file))
#     st.image(editor.oilpainting(file))
#     img_sepia = editor.sepia(file)
#     st.image(img_sepia)
#     st.image(editor.sharpen(file))
#     st.image(editor.get_hdr(file))
#     st.image(editor.get_inverse(file))
#     st.image(editor.summer_effect(file))
#     st.image(editor.winter_effect(file))
