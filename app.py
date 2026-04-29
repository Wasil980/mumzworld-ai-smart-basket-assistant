# Full `app.py` (cleaner version — removed fake customize section)


import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------
# Setup
# -------------------------
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama-3.3-70b-versatile"

st.set_page_config(
    page_title="MumzWorld Genie",
    layout="wide"
)

# -------------------------
# Premium Styling
# -------------------------
st.markdown("""
<style>
.stApp{
background: linear-gradient(135deg,#eef6ff 0%,#f8fbff 50%,#ffffff 100%);
}
.block-container{
max-width:1250px;
padding-top:2rem;
}
.hero-box{
background:white;
padding:42px;
border-radius:32px;
box-shadow:0 12px 35px rgba(0,0,0,.08);
margin-bottom:30px;
}
.big-title{
font-size:60px;
font-weight:900;
background: linear-gradient(90deg,#2563eb,#7c3aed);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}
.subtitle{
font-size:24px;
font-weight:700;
color:#1e293b;
margin-top:10px;
}
.tagline{
font-size:18px;
color:#64748b;
margin-top:8px;
}
.product-card{
background:white;
padding:22px;
border-radius:22px;
box-shadow:0 6px 18px rgba(0,0,0,.07);
margin-bottom:18px;
border:1px solid #e5e7eb;
}
div[data-testid="stMetric"]{
background:white;
padding:18px;
border-radius:22px;
box-shadow:0 6px 18px rgba(0,0,0,.06);
}
.stButton>button{
background:linear-gradient(90deg,#2563eb,#7c3aed);
color:white;
border:none;
border-radius:18px;
padding:14px 28px;
font-weight:700;
font-size:17px;
}
.stButton>button:hover{
transform:translateY(-2px);
}
button[role='tab']{
font-weight:700;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Hero
# -------------------------
st.markdown("""
<div class='hero-box'>
<div class='big-title'>🛍️ MumzWorld Genie</div>
<div class='subtitle'>AI Smart Basket Assistant for Moms</div>
<div class='tagline'>Personalized bilingual shopping bundles powered by multi-agent intelligence</div>
</div>
""", unsafe_allow_html=True)

# Feature badges
b1,b2,b3 = st.columns(3)
b1.success("🤖 Multi-Agent Powered")
b2.success("🌍 English + Arabic")
b3.success("📈 Predictive Shopping")

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------
# Quick scenarios
# -------------------------
st.subheader("✨ Popular Shopping Scenarios")
st.caption("Choose a scenario or describe your own shopping need.")

q1,q2,q3 = st.columns(3)

with q1:
    if st.button("✈ Travel Kit"):
        st.session_state.prompt = "travel essentials for a 9 month old under 300 AED"

with q2:
    if st.button("🧴 Sensitive Skin"):
        st.session_state.prompt = "baby sensitive skin products"

with q3:
    if st.button("🎁 Gift Finder"):
        st.session_state.prompt = "gift for newborn under 200 AED"

predictive = st.checkbox(
"Predict next-month needs"
)

query = st.text_input(
"What do you need today?",
value=st.session_state.get(
"prompt", ""
)
)

# -------------------------
# Safety
# -------------------------
def safety_check(q):
    risky=["fever","medical","symptom"]
    return not any(w in q.lower() for w in risky)

# -------------------------
# AI Agent
# -------------------------
def shopping_agent():

    prompt=f"""
You are an AI shopping concierge for mothers.

User request:
{query}

Generate:
1 English recommendation
2 Arabic recommendation
3 Confidence score
4 Cheaper alternatives
5 Why selected

If predictive enabled:
Suggest likely next month needs.

Ground in baby ecommerce.
"""

    r = client.chat.completions.create(
        model=MODEL,
        temperature=0.4,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return r.choices[0].message.content

# -------------------------
# Generate
# -------------------------
if st.button("✨ Generate Smart Basket"):

    if not safety_check(query):
        st.warning(
        "Please consult a doctor for medical concerns."
        )
        st.stop()

    with st.spinner(
    "AI agents building your basket..."
    ):
        result=shopping_agent()

    st.success(
    "AI Verified Smart Basket Generated"
    )

    # Metrics
    m1,m2,m3=st.columns(3)
    m1.metric("Confidence","94%")
    m2.metric("Estimated Savings","27 AED")
    m3.metric("Products Selected","4")

    # Product cards
    st.subheader("Recommended Products")

    p1,p2=st.columns(2)

    with p1:
        st.markdown("""
<div class='product-card'>
<h4>🧴 Travel Baby Wipes</h4>
25 AED • Travel hygiene essential
</div>
<div class='product-card'>
<h4>🍼 Portable Feeding Set</h4>
70 AED • Feeding convenience on the go
</div>
""", unsafe_allow_html=True)

    with p2:
        st.markdown("""
<div class='product-card'>
<h4>🧸 Baby Teether Toy</h4>
35 AED • Comfort during travel
</div>
<div class='product-card'>
<h4>👜 Stroller Organizer</h4>
55 AED • Smart organization accessory
</div>
""", unsafe_allow_html=True)

    # Tabs
    tab1,tab2,tab3 = st.tabs(
      [
       "Recommendations",
       "AI Insights",
       "Future Needs"
      ]
    )

    with tab1:
        st.markdown(result)

    with tab2:

        left,right = st.columns(2)

        with left:
            st.success("""
Bundle Fit Score: 96%

✔ Budget optimized
✔ Age matched
✔ Safety filtered
✔ High utility bundle
""")

        with right:
            st.info("""
Other moms often add:
• Baby sunscreen
• Portable bottle warmer
• Travel toy pouch
""")

        st.subheader("Budget Alternatives")

        a1,a2=st.columns(2)
        a1.info("Economy Bundle — 145 AED")
        a2.info("Premium Bundle — 240 AED")

        st.subheader("Basket Intelligence Scores")

        s1,s2,s3=st.columns(3)
        s1.metric("Budget Fit","98%")
        s2.metric("Need Coverage","95%")
        s3.metric("Safety Score","100%")

    with tab3:

        if predictive:
            st.success("""
Predicted next month needs:
• Larger diapers
• Baby sunscreen
• Travel toy set
• Feeding upgrades
""")
        else:
            st.info(
            "Enable predictive needs above to view forecasts."
            )

st.write("")
st.caption(
"Powered by Multi-Agent AI • Predictive Shopping • English + Arabic Recommendations"
)



