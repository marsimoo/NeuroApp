import streamlit as st
import numpy as np
import time


st.set_page_config(page_title="NeuroWheels", layout="wide")

# App title
st.title("🧠 NeuroWheels")

# Sidebar menu
menu = st.sidebar.selectbox("Navigate", [
    "Welcome & Instructions",
    "Chat with NeuroGuide",
    "View Brain Signals",
    "Upgrade & Add-ons"
])

# Session state for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# 🧾 Welcome Screen + Instructions
# -------------------------------
if menu == "Welcome & Instructions":
    st.header("👋 Welcome to NeuroWheels!")
    st.subheader("Your Personal NeuroCompanion")

    st.markdown("Hi there! I'm **NeuroGuide**, here to help you monitor, understand, and interact with your brain signals through our AI-powered assistant and signal viewer.")

    if st.button("🧾 Show My Info"):
        with st.expander("Your Profile"):
            st.write("**Name:** Mariam Kandari")
            st.write("**Usage Type:** Caregiver / Researcher")
            st.write("**Last Session:** April 17, 2025")
            st.write("**Connected Device:** BITalino EEG Kit")
            st.success("You're all set and connected!")

    st.divider()

    st.subheader("🛠 How to Use This App")
    st.markdown("""
    - 👉 **Chat with NeuroGuide**
    - 📊 **Health Check-Ups**
    - 🎯 **Unlock Features**
    """)

# -------------------------------
# 🤖 Chatbot Section (NeuroGuide)
# -------------------------------
elif menu == "Chat with NeuroGuide":
    st.header("🤖 NeuroGuide - Your Brainy Assistant")
    user_input = st.chat_input("Ask NeuroGuide anything...")


# -------------------------------
# 📈 Brain Signal Visualization
# -------------------------------
elif menu == "View Brain Signals":
    st.header("📊 Real-Time BioSignal Dashboard")
    placeholder = st.empty()

    for _ in range(100):  # Simulate live updates
        t = np.linspace(0, 2, 256)
        brain_wave = np.sin(2 * np.pi * (10 + np.random.rand()) * t) + 0.3 * np.random.randn(len(t))

        heart_rate = np.random.randint(65, 100)
        breathing_rate = np.random.randint(12, 20)
        stress_level = np.random.uniform(0, 1)
        overall_health = "Good" if stress_level < 0.6 else "Moderate" if stress_level < 0.8 else "Stressed"

        with placeholder.container():
            st.subheader("🧠 Brainwave Signal")
            fig, ax = plt.subplots()
            ax.plot(t, brain_wave)
            ax.set_ylim([-3, 3])
            ax.set_xlabel("Time (s)")
            ax.set_ylabel("Amplitude")
            ax.set_title("Live EEG-like Signal")
            st.pyplot(fig)

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("❤️ Heart Rate", f"{heart_rate} bpm")
            col2.metric("💨 Breathing", f"{breathing_rate} rpm")
            col3.metric("😬 Stress", f"{stress_level:.2f}")
            col4.metric("🧑‍⚕️ Health", overall_health)

            st.info("⏳ Streaming live simulated data...")

        time.sleep(0.1)
# -------------------------------
# 💳 Upgrade & Add-on Features
# -------------------------------
elif menu == "Upgrade & Add-ons":
    st.header("💳 Upgrade to Premium & Add Features")

    st.markdown("**Enjoy enhanced functionality by upgrading or adding hardware to your NeuroWheels experience.**")

    st.subheader("🧠 Premium Version")
    upgrade = st.checkbox("Upgrade to Premium (5 KD)", value=False)

    st.subheader("🛒 Additional Features")
    buy_arm = st.checkbox("Add Robotic Arm (45 KD)", value=False)
    buy_tablet = st.checkbox("Add Built-in Tablet (30 KD)", value=False)

    # Calculate total
    total = 0
    if upgrade:
        total += 5
    if buy_arm:
        total += 45
    if buy_tablet:
        total += 30

    st.divider()

    st.subheader("🧾 Order Summary")
    if total == 0:
        st.info("No upgrades or add-ons selected.")
    else:
        st.success(f"Total: {total} KD")
        if st.button("Proceed to Payment"):
            st.balloons()
            st.success("Thank you! Your upgrades will be activated shortly.")
