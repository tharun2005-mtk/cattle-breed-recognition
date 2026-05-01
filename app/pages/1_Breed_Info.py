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

# def get_best_image(folder, count=3):
#     """Get the clearest image from the folder by picking middle ones (avoid corrupted first/last)"""
#     try:
#         files = sorted([f for f in os.listdir(folder)
#                  if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
#         if not files:
#             return None
#         # Pick from middle of the list for better quality images
#         mid = len(files) // 2
#         for i in range(mid, min(mid + count, len(files))):
#             try:
#                 img = PILImage.open(os.path.join(folder, files[i]))
#                 img.verify()
#                 # Reopen after verify
#                 img = PILImage.open(os.path.join(folder, files[i]))
#                 return img
#             except:
#                 continue
#     except:
#         pass
#     return None

# # ── Display Breeds ───────────────────────────────────
# for breed in filtered:
#     col1, col2 = st.columns([1, 2])

#     with col1:
#         img = get_best_image(breed["folder"])
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
#         "fact": "One of the most popular Zebu breeds exported worldwide.",
#         "image": "https://girorganic.com/cdn/shop/articles/what-is-gir-cow-453725.jpg?v=1673547600 | ",
#         "search_url": "https://www.google.com/search?q=Gir+cow+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Sahiwal Cow",
#         "type": "🐄 Cattle",
#         "origin": "Punjab, India & Pakistan",
#         "color": "Reddish brown",
#         "milk": "8–14 litres/day",
#         "use": "Dairy",
#         "fact": "Considered the best dairy breed in India.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/sahiwal.jpg",
#         "search_url": "https://www.google.com/search?q=Sahiwal+cow+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Ongole Cow",
#         "type": "🐄 Cattle",
#         "origin": "Andhra Pradesh, India",
#         "color": "White/Grey",
#         "milk": "5–8 litres/day",
#         "use": "Draught & Dairy",
#         "fact": "Known for massive body size and strength.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/ongole.jpg",
#         "search_url": "https://www.google.com/search?q=Ongole+cow+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Kankrej Cow",
#         "type": "🐄 Cattle",
#         "origin": "Gujarat & Rajasthan, India",
#         "color": "Silver grey to steel grey",
#         "milk": "6–10 litres/day",
#         "use": "Dual purpose",
#         "fact": "One of the heaviest Indian breeds.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/kankrej.jpg",
#         "search_url": "https://www.google.com/search?q=Kankrej+cow+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Tharparkar Cow",
#         "type": "🐄 Cattle",
#         "origin": "Rajasthan, India",
#         "color": "White to grey",
#         "milk": "6–10 litres/day",
#         "use": "Dual purpose",
#         "fact": "Highly adapted to arid desert conditions.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/tharparkar.jpg",
#         "search_url": "https://www.google.com/search?q=Tharparkar+cow+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Murrah Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Haryana, India",
#         "color": "Jet black",
#         "milk": "15–25 litres/day",
#         "use": "Dairy",
#         "fact": "World's highest milk-producing buffalo.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/murrah.jpg",
#         "search_url": "https://www.google.com/search?q=Murrah+buffalo+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Nili-Ravi Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Punjab, India & Pakistan",
#         "color": "Black with white markings",
#         "milk": "12–18 litres/day",
#         "use": "Dairy",
#         "fact": "Known for very high fat content in milk.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/niliravi.jpg",
#         "search_url": "https://www.google.com/search?q=Nili+Ravi+buffalo+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Surti Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Gujarat, India",
#         "color": "Rust brown to silver grey",
#         "milk": "8–12 litres/day",
#         "use": "Dairy",
#         "fact": "Medium sized buffalo known for good quality milk.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/surti.jpg",
#         "search_url": "https://www.google.com/search?q=Surti+buffalo+India+breed+info&tbm=isch"
#     },
#     {
#         "name": "Jaffarabadi Buffalo",
#         "type": "🐃 Buffalo",
#         "origin": "Gujarat, India",
#         "color": "Black",
#         "milk": "10–15 litres/day",
#         "use": "Dairy",
#         "fact": "Heaviest buffalo breed in India.",
#         "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/jaffarabadi.jpg",
#         "search_url": "https://www.google.com/search?q=Jaffarabadi+buffalo+India+breed+info&tbm=isch"
#     }
# ]

# # 🔍 Filter
# filter_type = st.radio(
#     "Filter by type:",
#     ["All", "🐄 Cattle Only", "🐃 Buffalo Only"],
#     horizontal=True
# )

# if filter_type == "🐄 Cattle Only":
#     filtered = [b for b in breeds if b["type"] == "🐄 Cattle"]
# elif filter_type == "🐃 Buffalo Only":
#     filtered = [b for b in breeds if b["type"] == "🐃 Buffalo"]
# else:
#     filtered = breeds

# st.markdown(f"Showing **{len(filtered)}** breeds")
# st.markdown("---")

# # 📊 Display
# for breed in filtered:
#     col1, col2 = st.columns([1, 2])

#     with col1:
#         st.image(breed["image"], use_container_width=True, caption=breed["name"])

#     with col2:
#         st.subheader(f"{breed['type']} — {breed['name']}")
#         st.markdown(f"📍 **Origin:** {breed['origin']}")
#         st.markdown(f"🎨 **Color:** {breed['color']}")
#         st.markdown(f"🥛 **Milk Yield:** {breed['milk']}")
#         st.markdown(f"⚙️ **Primary Use:** {breed['use']}")
#         st.success(f"💡 **Interesting Fact:** {breed['fact']}")

#         col_btn1, col_btn2 = st.columns(2)
#         with col_btn1:
#             st.link_button("🔍 Search on Google", breed['search_url'])
#         with col_btn2:
#             wiki_url = f"https://en.wikipedia.org/wiki/{breed['name'].replace(' ', '_')}"
#             st.link_button("📖 Wikipedia", wiki_url)

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

# 📁 Load local image based on breed name
def get_local_image(breed_name):
    folder_map = {
        "Gir Cow": "dataset/train/Gir_cow_India",
        "Sahiwal Cow": "dataset/train/Sahiwal_cow_India",
        "Ongole Cow": "dataset/train/Ongole_cow_India",
        "Kankrej Cow": "dataset/train/Kankrej_cow_India",
        "Tharparkar Cow": "dataset/train/Tharparkar_cow_India",
        "Murrah Buffalo": "dataset/train/Murrah_buffalo_India",
        "Nili-Ravi Buffalo": "dataset/train/Nili_Ravi_buffalo_India",
        "Surti Buffalo": "dataset/train/Surti_buffalo_India",
        "Jaffarabadi Buffalo": "dataset/train/Jaffarabadi_buffalo_India"
    }

    folder = folder_map.get(breed_name)

    try:
        files = [f for f in os.listdir(folder)
                 if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if files:
            return PILImage.open(os.path.join(folder, files[0]))
    except:
        return None

    return None


# ✅ All 9 breeds
breeds = [
    {
        "name": "Gir Cow",
        "type": "🐄 Cattle",
        "origin": "Gujarat, India",
        "color": "Red/Yellow with dark spots",
        "milk": "10–16 litres/day",
        "use": "Dairy",
        # "fact": "One of the most popular Zebu breeds exported worldwide.",
        "fact": "One of the most popular Zebu breeds exported worldwide. Used to improve Brazilian cattle.",
        "image": "https://girorganic.com/cdn/shop/articles/what-is-gir-cow-453725.jpg?v=1673547600",
        "search_url": "https://www.google.com/search?q=Gir+cow+India"
    },
    {
        "name": "Sahiwal Cow",
        "type": "🐄 Cattle",
        "origin": "Punjab, India & Pakistan",
        "color": "Reddish brown",
        "milk": "8–14 litres/day",
        "use": "Dairy",
        # "fact": "Best dairy breed in India.",
        "fact": "Considered the best dairy breed in India. Highly resistant to tick-borne diseases.",
        "image": "https://docs.krishnayangauraksha.org/blog/09_08_2024_15_13_37_What%20is%20Sahiwal%20Cow.jpg",
        "search_url": "https://www.google.com/search?q=Sahiwal+cow"
    },
    {
        "name": "Ongole Cow",
        "type": "🐄 Cattle",
        "origin": "Andhra Pradesh",
        "color": "White/Grey",
        "milk": "5–8 litres/day",
        "use": "Draught & Dairy",
        # "fact": "Known for strength.",
        "fact": "Known for massive body size and strength. Widely exported to Brazil and USA.",
        "image": "data:image/jpeg;base64,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",
        "search_url": "https://www.google.com/search?q=Ongole+cow"
    },
    {
        "name": "Kankrej Cow",
        "type": "🐄 Cattle",
        "origin": "Gujarat & Rajasthan",
        "color": "Grey",
        "milk": "6–10 litres/day",
        "use": "Dual purpose",
        # "fact": "Heavy breed.",
        "fact": "One of the heaviest Indian breeds. Bulls are famous for fast and powerful draught work.",
        "image": "https://cpimg.tistatic.com/3814100/b/5/kankrej-cows.jpg",
        "search_url": "https://www.google.com/search?q=Kankrej+cow"
    },
    {
        "name": "Tharparkar Cow",
        "type": "🐄 Cattle",
        "origin": "Rajasthan",
        "color": "White",
        "milk": "6–10 litres/day",
        "use": "Dual purpose",
        # "fact": "Desert adapted.",
        "fact": "Highly adapted to arid desert conditions. Can survive on minimal water and food.",
        "image": "https://www.a2milkbasket.com/images/tharparker-cow-milk-noida.jpg",
        "search_url": "https://www.google.com/search?q=Tharparkar+cow"
    },
    {
        "name": "Murrah Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Haryana",
        "color": "Black",
        "milk": "15–25 litres/day",
        "use": "Dairy",
        # "fact": "Highest milk producer.",
        "fact": "World's highest milk-producing buffalo. Milk has 7% fat content — ideal for ghee and butter.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvisZON2MEaVcgro6gX8cHaBdmqNje3uM5Dg&s",
        "search_url": "https://www.google.com/search?q=Murrah+buffalo"
    },
    {
        "name": "Nili-Ravi Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Punjab",
        "color": "Black with white",
        "milk": "12–18 litres/day",
        "use": "Dairy",
        # "fact": "High fat milk.",
        "fact": "Known for very high fat content in milk. Second most popular buffalo breed in India.",
        "image": "https://hisarbovine.com/downloads/faculty/n6791ee07a6973.jpg",
        "search_url": "https://www.google.com/search?q=Nili+Ravi+buffalo"
    },
    {
        "name": "Surti Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Gujarat",
        "color": "Brown/Grey",
        "milk": "8–12 litres/day",
        "use": "Dairy",
        # "fact": "Good milk.",
        "fact": "Medium sized buffalo known for good quality milk. Mainly found in Vadodara and Surat districts.",
        "image": "data:image/jpeg;base64,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",
        "search_url": "https://www.google.com/search?q=Surti+buffalo"
    },
    {
        "name": "Jaffarabadi Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Gujarat",
        "color": "Black",
        "milk": "10–15 litres/day",
        "use": "Dairy",
        # "fact": "Heaviest buffalo.",
        "fact": "Heaviest buffalo breed in India. Named after Jafarabad town in Gir Somnath district.",
        "image": "data:image/jpeg;base64,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",
        "search_url": "https://www.google.com/search?q=Jaffarabadi+buffalo"
    }
]

# 🔍 Filter
filter_type = st.radio(
    "Filter by type:",
    ["All", "🐄 Cattle Only", "🐃 Buffalo Only"],
    horizontal=True
)

if filter_type == "🐄 Cattle Only":
    filtered = [b for b in breeds if b["type"] == "🐄 Cattle"]
elif filter_type == "🐃 Buffalo Only":
    filtered = [b for b in breeds if b["type"] == "🐃 Buffalo"]
else:
    filtered = breeds

st.markdown(f"Showing **{len(filtered)}** breeds")
st.markdown("---")

# 📊 Display
for breed in filtered:
    col1, col2 = st.columns([1, 2])

    with col1:
        try:
            st.image(breed["image"], use_container_width=True)
        except:
            img = get_local_image(breed["name"])
            if img:
                st.image(img, use_container_width=True)
            else:
                st.warning("Image not available")

    with col2:
        st.subheader(f"{breed['type']} — {breed['name']}")
        st.markdown(f"📍 **Origin:** {breed['origin']}")
        st.markdown(f"🎨 **Color:** {breed['color']}")
        st.markdown(f"🥛 **Milk Yield:** {breed['milk']}")
        st.markdown(f"⚙️ **Use:** {breed['use']}")
        # st.success(f"💡 {breed['fact']}")
        st.success(f"💡 **Interesting Fact:** {breed['fact']}")

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.link_button("🔍 Google", breed["search_url"])
        with col_btn2:
            wiki_url = f"https://en.wikipedia.org/wiki/{breed['name'].replace(' ', '_')}"
            st.link_button("📖 Wikipedia", wiki_url)

    st.markdown("---")