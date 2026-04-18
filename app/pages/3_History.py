import streamlit as st

st.set_page_config(
    page_title="📜 Prediction History",
    page_icon="📜",
    layout="centered"
)

st.title("📜 Prediction History")
st.markdown("Last **5 predictions** made in this session.")
st.markdown("---")

# ── Check History ────────────────────────────────────
if "history" not in st.session_state or len(st.session_state.history) == 0:
    st.info("📭 No predictions yet! Go to the **Home page** and upload an image first.")
    st.markdown("👈 Click **app** in the sidebar to go back to home!")

else:
    st.success(f"✅ {len(st.session_state.history)} prediction(s) found!")
    st.markdown("---")

    # ── Show history in reverse (latest first) ───────
    for i, record in enumerate(reversed(st.session_state.history)):
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(record["image"], width='stretch')

        with col2:
            st.subheader(f"🔍 Prediction #{len(st.session_state.history) - i}")
            st.success(f"✅ **{record['breed']}**")
            st.metric("Confidence", record["confidence"])
            st.caption(f"🕐 Time: {record['time']}")

        st.markdown("---")

    # ── Clear History Button ──────────────────────────
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.success("✅ History cleared!")
        st.rerun()