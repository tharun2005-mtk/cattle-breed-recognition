# import streamlit as st

# st.set_page_config(
#     page_title="🐄 Breed Info",
#     page_icon="📖",
#     layout="wide"
# )

# st.title("📖 Indian Cattle & Buffalo Breeds — Complete Guide")
# st.markdown("Detailed information about all 9 breeds supported by our AI model.")
# st.markdown("---")

# breeds = [
#     {
#         "name": "Gir Cow",
#         "type": "🐄 Cattle",
#         "origin": "Gujarat, India",
#         "color": "Red/Yellow with dark spots",
#         "milk": "10–16 litres/day",
#         "use": "Dairy",
#         "fact": "One of the most popular Zebu breeds exported worldwide. Used to improve Brazilian cattle.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Gyr_Bull.jpg/320px-Gyr_Bull.jpg"
#     },
#     {
#         "name": "Sahiwal Cow",
#         "type": "🐄 Cattle",
#         "origin": "Punjab, India & Pakistan",
#         "color": "Reddish brown",
#         "milk": "8–14 litres/day",
#         "use": "Dairy",
#         "fact": "Considered the best dairy breed in India. Highly resistant to tick-borne diseases.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Sahiwal_Bull.jpg/320px-Sahiwal_Bull.jpg"
#     },
#     {
#         "name": "Ongole Cow",
#         "type": "🐄 Cattle",
#         "origin": "Andhra Pradesh, India",
#         "color": "White/Grey",
#         "milk": "5–8 litres/day",
#         "use": "Draught & Dairy",
#         "fact": "Known for massive body size and strength. Widely exported to Brazil and USA.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Ongole_Bull.jpg/320px-Ongole_Bull.jpg"
#     },
#     {
#         "name": "Kankrej Cow",
#         "type": "🐄 Cattle",
#         "origin": "Gujarat & Rajasthan, India",
#         "color": "Silver grey to steel grey",
#         "milk": "6–10 litres/day",
#         "use": "Dual purpose",
#         "fact": "One of the heaviest Indian breeds. Bulls are famous for fast and powerful draught work.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Kankrej_bull.jpg/320px-Kankrej_bull.jpg"
#     },
#     {
#         "name": "Tharparkar Cow",
#         "type": "🐄 Cattle",
#         "origin": "Rajasthan, India",
#         "color": "White to grey",
#         "milk": "6–10 litres/day",
#         "use": "Dual purpose",
#         "fact": "Highly adapted to arid desert conditions. Can survive on minimal water and food.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Tharparkar_cow.jpg/320px-Tharparkar_cow.jpg"
#     },
#     {
#         "name": "Murrah Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Haryana, India",
#         "color": "Jet black",
#         "milk": "15–25 litres/day",
#         "use": "Dairy",
#         "fact": "World's highest milk-producing buffalo. Milk has 7% fat content — ideal for ghee and butter.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Murrah_Buffalo.jpg/320px-Murrah_Buffalo.jpg"
#     },
#     {
#         "name": "Nili-Ravi Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Punjab, India & Pakistan",
#         "color": "Black with white markings",
#         "milk": "12–18 litres/day",
#         "use": "Dairy",
#         "fact": "Known for very high fat content in milk. Second most popular buffalo breed in India.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Nili_Ravi_Buffalo.jpg/320px-Nili_Ravi_Buffalo.jpg"
#     },
#     {
#         "name": "Surti Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Gujarat, India",
#         "color": "Rust brown to silver grey",
#         "milk": "8–12 litres/day",
#         "use": "Dairy",
#         "fact": "Medium sized buffalo known for good quality milk. Mainly found in Vadodara and Surat districts.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Surti_buffalo.jpg/320px-Surti_buffalo.jpg"
#     },
#     {
#         "name": "Jaffarabadi Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Gujarat, India",
#         "color": "Black",
#         "milk": "10–15 litres/day",
#         "use": "Dairy",
#         "fact": "Heaviest buffalo breed in India. Named after Jafarabad town in Gir Somnath district.",
#         "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Jaffarabadi_buffalo.jpg/320px-Jaffarabadi_buffalo.jpg"
#     }
# ]

# # ── Filter ───────────────────────────────────────────
# filter_type = st.radio(
#     "Filter by type:",
#     ["All", "🐄 Cattle Only", "🐃 Buffalo Only"],
#     horizontal=True
# )

# filtered = breeds
# if filter_type == "🐄 Cattle Only":
#     filtered = [b for b in breeds if b["type"] == "🐄 Cattle"]
# elif filter_type == "🐃 Buffalo Only":
#     filtered = [b for b in breeds if b["type"] == "🐃 Buffalo"]

# st.markdown(f"Showing **{len(filtered)}** breeds")
# st.markdown("---")

# # ── Display Breeds ───────────────────────────────────
# for breed in filtered:
#     col1, col2 = st.columns([1, 2])

#     with col1:
#         try:
#             st.image(breed["image"], use_container_width=True, caption=breed["name"])
#         except:
#             st.info("Image not available")

#     with col2:
#         st.subheader(f"{breed['type']} — {breed['name']}")
#         st.markdown(f"📍 **Origin:** {breed['origin']}")
#         st.markdown(f"🎨 **Color:** {breed['color']}")
#         st.markdown(f"🥛 **Milk Yield:** {breed['milk']}")
#         st.markdown(f"⚙️ **Primary Use:** {breed['use']}")
#         st.success(f"💡 **Interesting Fact:** {breed['fact']}")

#     st.markdown("---")

# import streamlit as st
# import os
# from PIL import Image as PILImage

# st.set_page_config(
#     page_title="🐄 Breed Info",
#     page_icon="📖",
#     layout="wide"
# )

# st.title("📖 Indian Cattle & Buffalo Breeds — Complete Guide")
# st.markdown("Detailed information about all 9 breeds supported by our AI model.")
# st.markdown("---")

# breeds = [
#     {
#         "name": "Gir Cow", "type": "🐄 Cattle", "origin": "Gujarat, India",
#         "color": "Red/Yellow with dark spots", "milk": "10–16 litres/day", "use": "Dairy",
#         "fact": "One of the most popular Zebu breeds exported worldwide. Used to improve Brazilian cattle.",
#         "folder": "dataset/train/Gir_cow_India"
#     },
#     {
#         "name": "Sahiwal Cow", "type": "🐄 Cattle", "origin": "Punjab, India & Pakistan",
#         "color": "Reddish brown", "milk": "8–14 litres/day", "use": "Dairy",
#         "fact": "Considered the best dairy breed in India. Highly resistant to tick-borne diseases.",
#         "folder": "dataset/train/Sahiwal_cow_India"
#     },
#     {
#         "name": "Ongole Cow", "type": "🐄 Cattle", "origin": "Andhra Pradesh, India",
#         "color": "White/Grey", "milk": "5–8 litres/day", "use": "Draught & Dairy",
#         "fact": "Known for massive body size and strength. Widely exported to Brazil and USA.",
#         "folder": "dataset/train/Ongole_cow_India"
#     },
#     {
#         "name": "Kankrej Cow", "type": "🐄 Cattle", "origin": "Gujarat & Rajasthan, India",
#         "color": "Silver grey to steel grey", "milk": "6–10 litres/day", "use": "Dual purpose",
#         "fact": "One of the heaviest Indian breeds. Bulls are famous for fast and powerful draught work.",
#         "folder": "dataset/train/Kankrej_cow_India"
#     },
#     {
#         "name": "Tharparkar Cow", "type": "🐄 Cattle", "origin": "Rajasthan, India",
#         "color": "White to grey", "milk": "6–10 litres/day", "use": "Dual purpose",
#         "fact": "Highly adapted to arid desert conditions. Can survive on minimal water and food.",
#         "folder": "dataset/train/Tharparkar_cow_India"
#     },
#     {
#         "name": "Murrah Buffalo", "type": "🐃 Buffalo", "origin": "Haryana, India",
#         "color": "Jet black", "milk": "15–25 litres/day", "use": "Dairy",
#         "fact": "World's highest milk-producing buffalo. Milk has 7% fat content — ideal for ghee and butter.",
#         "folder": "dataset/train/Murrah_buffalo_India"
#     },
#     {
#         "name": "Nili-Ravi Buffalo", "type": "🐃 Buffalo", "origin": "Punjab, India & Pakistan",
#         "color": "Black with white markings", "milk": "12–18 litres/day", "use": "Dairy",
#         "fact": "Known for very high fat content in milk. Second most popular buffalo breed in India.",
#         "folder": "dataset/train/Nili_Ravi_buffalo_India"
#     },
#     {
#         "name": "Surti Buffalo", "type": "🐃 Buffalo", "origin": "Gujarat, India",
#         "color": "Rust brown to silver grey", "milk": "8–12 litres/day", "use": "Dairy",
#         "fact": "Medium sized buffalo known for good quality milk. Mainly found in Vadodara and Surat districts.",
#         "folder": "dataset/train/Surti_buffalo_India"
#     },
#     {
#         "name": "Jaffarabadi Buffalo", "type": "🐃 Buffalo", "origin": "Gujarat, India",
#         "color": "Black", "milk": "10–15 litres/day", "use": "Dairy",
#         "fact": "Heaviest buffalo breed in India. Named after Jafarabad town in Gir Somnath district.",
#         "folder": "dataset/train/Jaffarabadi_buffalo_India"
#     }
# ]

# # ── Filter ───────────────────────────────────────────
# filter_type = st.radio(
#     "Filter by type:",
#     ["All", "🐄 Cattle Only", "🐃 Buffalo Only"],
#     horizontal=True
# )

# filtered = breeds
# if filter_type == "🐄 Cattle Only":
#     filtered = [b for b in breeds if b["type"] == "🐄 Cattle"]
# elif filter_type == "🐃 Buffalo Only":
#     filtered = [b for b in breeds if b["type"] == "🐃 Buffalo"]

# st.markdown(f"Showing **{len(filtered)}** breeds")
# st.markdown("---")

# def get_first_image(folder):
#     try:
#         files = [f for f in os.listdir(folder)
#                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
#         if files:
#             return PILImage.open(os.path.join(folder, files[0]))
#     except:
#         pass
#     return None

# # ── Display Breeds ───────────────────────────────────
# for breed in filtered:
#     col1, col2 = st.columns([1, 2])

#     with col1:
#         img = get_first_image(breed["folder"])
#         if img:
#             st.image(img, use_container_width=True, caption=breed["name"])
#         else:
#             st.info("Image not available")

#     with col2:
#         st.subheader(f"{breed['type']} — {breed['name']}")
#         st.markdown(f"📍 **Origin:** {breed['origin']}")
#         st.markdown(f"🎨 **Color:** {breed['color']}")
#         st.markdown(f"🥛 **Milk Yield:** {breed['milk']}")
#         st.markdown(f"⚙️ **Primary Use:** {breed['use']}")
#         st.success(f"💡 **Interesting Fact:** {breed['fact']}")

#     st.markdown("---")

import streamlit as st
import os
from PIL import Image as PILImage

st.set_page_config(
    page_title="🐄 Breed Info",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Indian Cattle & Buffalo Breeds — Complete Guide")
st.markdown("Detailed information about all 9 breeds supported by our AI model.")
st.markdown("---")

breeds = [
    {
        "name": "Gir Cow", "type": "🐄 Cattle", "origin": "Gujarat, India",
        "color": "Red/Yellow with dark spots", "milk": "10–16 litres/day", "use": "Dairy",
        "fact": "One of the most popular Zebu breeds exported worldwide. Used to improve Brazilian cattle.",
        "folder": "dataset/train/Gir_cow_India"
    },
    {
        "name": "Sahiwal Cow", "type": "🐄 Cattle", "origin": "Punjab, India & Pakistan",
        "color": "Reddish brown", "milk": "8–14 litres/day", "use": "Dairy",
        "fact": "Considered the best dairy breed in India. Highly resistant to tick-borne diseases.",
        "folder": "dataset/train/Sahiwal_cow_India"
    },
    {
        "name": "Ongole Cow", "type": "🐄 Cattle", "origin": "Andhra Pradesh, India",
        "color": "White/Grey", "milk": "5–8 litres/day", "use": "Draught & Dairy",
        "fact": "Known for massive body size and strength. Widely exported to Brazil and USA.",
        "folder": "dataset/train/Ongole_cow_India"
    },
    {
        "name": "Kankrej Cow", "type": "🐄 Cattle", "origin": "Gujarat & Rajasthan, India",
        "color": "Silver grey to steel grey", "milk": "6–10 litres/day", "use": "Dual purpose",
        "fact": "One of the heaviest Indian breeds. Bulls are famous for fast and powerful draught work.",
        "folder": "dataset/train/Kankrej_cow_India"
    },
    {
        "name": "Tharparkar Cow", "type": "🐄 Cattle", "origin": "Rajasthan, India",
        "color": "White to grey", "milk": "6–10 litres/day", "use": "Dual purpose",
        "fact": "Highly adapted to arid desert conditions. Can survive on minimal water and food.",
        "folder": "dataset/train/Tharparkar_cow_India"
    },
    {
        "name": "Murrah Buffalo", "type": "🐃 Buffalo", "origin": "Haryana, India",
        "color": "Jet black", "milk": "15–25 litres/day", "use": "Dairy",
        "fact": "World's highest milk-producing buffalo. Milk has 7% fat content — ideal for ghee and butter.",
        "folder": "dataset/train/Murrah_buffalo_India"
    },
    {
        "name": "Nili-Ravi Buffalo", "type": "🐃 Buffalo", "origin": "Punjab, India & Pakistan",
        "color": "Black with white markings", "milk": "12–18 litres/day", "use": "Dairy",
        "fact": "Known for very high fat content in milk. Second most popular buffalo breed in India.",
        "folder": "dataset/train/Nili_Ravi_buffalo_India"
    },
    {
        "name": "Surti Buffalo", "type": "🐃 Buffalo", "origin": "Gujarat, India",
        "color": "Rust brown to silver grey", "milk": "8–12 litres/day", "use": "Dairy",
        "fact": "Medium sized buffalo known for good quality milk. Mainly found in Vadodara and Surat districts.",
        "folder": "dataset/train/Surti_buffalo_India"
    },
    {
        "name": "Jaffarabadi Buffalo", "type": "🐃 Buffalo", "origin": "Gujarat, India",
        "color": "Black", "milk": "10–15 litres/day", "use": "Dairy",
        "fact": "Heaviest buffalo breed in India. Named after Jafarabad town in Gir Somnath district.",
        "folder": "dataset/train/Jaffarabadi_buffalo_India"
    }
]

# ── Filter ───────────────────────────────────────────
filter_type = st.radio(
    "Filter by type:",
    ["All", "🐄 Cattle Only", "🐃 Buffalo Only"],
    horizontal=True
)

filtered = breeds
if filter_type == "🐄 Cattle Only":
    filtered = [b for b in breeds if b["type"] == "🐄 Cattle"]
elif filter_type == "🐃 Buffalo Only":
    filtered = [b for b in breeds if b["type"] == "🐃 Buffalo"]

st.markdown(f"Showing **{len(filtered)}** breeds")
st.markdown("---")

def get_best_image(folder, count=3):
    """Get the clearest image from the folder by picking middle ones (avoid corrupted first/last)"""
    try:
        files = sorted([f for f in os.listdir(folder)
                 if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        if not files:
            return None
        # Pick from middle of the list for better quality images
        mid = len(files) // 2
        for i in range(mid, min(mid + count, len(files))):
            try:
                img = PILImage.open(os.path.join(folder, files[i]))
                img.verify()
                # Reopen after verify
                img = PILImage.open(os.path.join(folder, files[i]))
                return img
            except:
                continue
    except:
        pass
    return None

# ── Display Breeds ───────────────────────────────────
for breed in filtered:
    col1, col2 = st.columns([1, 2])

    with col1:
        img = get_best_image(breed["folder"])
        if img:
            st.image(img, use_container_width=True, caption=breed["name"])
        else:
            st.info("Image not available")

    with col2:
        st.subheader(f"{breed['type']} — {breed['name']}")
        st.markdown(f"📍 **Origin:** {breed['origin']}")
        st.markdown(f"🎨 **Color:** {breed['color']}")
        st.markdown(f"🥛 **Milk Yield:** {breed['milk']}")
        st.markdown(f"⚙️ **Primary Use:** {breed['use']}")
        st.success(f"💡 **Interesting Fact:** {breed['fact']}")

    st.markdown("---")