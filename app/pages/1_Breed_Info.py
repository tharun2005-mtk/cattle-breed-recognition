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
        "name": "Gir Cow",
        "type": "🐄 Cattle",
        "origin": "Gujarat, India",
        "color": "Red/Yellow with dark spots",
        "milk": "10–16 litres/day",
        "use": "Dairy",
        "fact": "One of the most popular Zebu breeds exported worldwide.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/gir.jpg",
        "search_url": "https://www.google.com/search?q=Gir+cow+India+breed+info&tbm=isch"
    },
    {
        "name": "Sahiwal Cow",
        "type": "🐄 Cattle",
        "origin": "Punjab, India & Pakistan",
        "color": "Reddish brown",
        "milk": "8–14 litres/day",
        "use": "Dairy",
        "fact": "Considered the best dairy breed in India.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/sahiwal.jpg",
        "search_url": "https://www.google.com/search?q=Sahiwal+cow+India+breed+info&tbm=isch"
    },
    {
        "name": "Ongole Cow",
        "type": "🐄 Cattle",
        "origin": "Andhra Pradesh, India",
        "color": "White/Grey",
        "milk": "5–8 litres/day",
        "use": "Draught & Dairy",
        "fact": "Known for massive body size and strength.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/ongole.jpg",
        "search_url": "https://www.google.com/search?q=Ongole+cow+India+breed+info&tbm=isch"
    },
    {
        "name": "Kankrej Cow",
        "type": "🐄 Cattle",
        "origin": "Gujarat & Rajasthan, India",
        "color": "Silver grey to steel grey",
        "milk": "6–10 litres/day",
        "use": "Dual purpose",
        "fact": "One of the heaviest Indian breeds.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/kankrej.jpg",
        "search_url": "https://www.google.com/search?q=Kankrej+cow+India+breed+info&tbm=isch"
    },
    {
        "name": "Tharparkar Cow",
        "type": "🐄 Cattle",
        "origin": "Rajasthan, India",
        "color": "White to grey",
        "milk": "6–10 litres/day",
        "use": "Dual purpose",
        "fact": "Highly adapted to arid desert conditions.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/tharparkar.jpg",
        "search_url": "https://www.google.com/search?q=Tharparkar+cow+India+breed+info&tbm=isch"
    },
    {
        "name": "Murrah Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Haryana, India",
        "color": "Jet black",
        "milk": "15–25 litres/day",
        "use": "Dairy",
        "fact": "World's highest milk-producing buffalo.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/murrah.jpg",
        "search_url": "https://www.google.com/search?q=Murrah+buffalo+India+breed+info&tbm=isch"
    },
    {
        "name": "Nili-Ravi Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Punjab, India & Pakistan",
        "color": "Black with white markings",
        "milk": "12–18 litres/day",
        "use": "Dairy",
        "fact": "Known for very high fat content in milk.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/niliravi.jpg",
        "search_url": "https://www.google.com/search?q=Nili+Ravi+buffalo+India+breed+info&tbm=isch"
    },
    {
        "name": "Surti Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Gujarat, India",
        "color": "Rust brown to silver grey",
        "milk": "8–12 litres/day",
        "use": "Dairy",
        "fact": "Medium sized buffalo known for good quality milk.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/surti.jpg",
        "search_url": "https://www.google.com/search?q=Surti+buffalo+India+breed+info&tbm=isch"
    },
    {
        "name": "Jaffarabadi Buffalo",
        "type": "🐃 Buffalo",
        "origin": "Gujarat, India",
        "color": "Black",
        "milk": "10–15 litres/day",
        "use": "Dairy",
        "fact": "Heaviest buffalo breed in India.",
        "image": "https://www.indiaagronet.com/indiaagronet/livestock/IMAGES/jaffarabadi.jpg",
        "search_url": "https://www.google.com/search?q=Jaffarabadi+buffalo+India+breed+info&tbm=isch"
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

    # ── Learn More Button ─────────────────────────
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.link_button("🔍 Search on Google", breed['search_url'])
    with col_btn2:
        wiki_url = f"https://en.wikipedia.org/wiki/{breed['name'].replace(' ', '_')}"
        st.link_button("📖 Wikipedia", wiki_url)
    st.markdown("---")