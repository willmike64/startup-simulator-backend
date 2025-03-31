# company_generator_ai.py — creates rich startup data via OpenAI

import openai
import streamlit as st
import random

openai.api_key = st.secrets["OPENAI_API_KEY"]

industries = [
    "AgTech", "EdTech", "HealthTech", "Clean Energy", "SaaS",
    "Consumer Goods", "eCommerce", "Biotech", "AI Tools", "Food Delivery",
    "Logistics", "RetailTech", "Greentech", "Mobility", "Digital Wellness","Coffee Shop", "Local Restaurant",
    "Fitness", "Real Estate", "TravelTech", "Fintech", "Manufacturing",
    "Construction", "Gaming", "Entertainment", "Telecom", "Cybersecurity",
    "Insurance", "LegalTech", "HRTech", "PropTech", "Blockchain",
    "Social Media", "Wearables", "Augmented Reality", "Virtual Reality",
    "Elder Care", "Pet Tech", "Travel", "Home Services", "Subscription Boxes",
    "Food & Beverage", "Fashion", "Beauty", "Sports", "Wellness",
    "Nonprofit", "Crowdfunding", "Digital Marketing", "Advertising",
    "Content Creation", "Influencer Marketing", "Event Planning", "Public Relations",
    "Market Research", "Data Analytics", "Artificial Intelligence",
    "Machine Learning", "Natural Language Processing", "Computer Vision",
    "Robotics", "Internet of Things", "Smart Home", "Smart City",
    "Telemedicine", "Health & Wellness", "Fitness & Nutrition",
    "Mental Health", "Personal Finance", "Investment", "Cryptocurrency",
    "Real Estate Investment", "Crowdfunding", "Peer-to-Peer Lending",
    "Wealth Management", "Insurance Tech", "RegTech", "Compliance",
    "Supply Chain", "Logistics & Transportation", "Fleet Management",
    "Last Mile Delivery", "E-commerce Logistics", "Warehouse Management",
    "Inventory Management", "Shipping & Freight", "Cold Chain Logistics",
    "Reverse Logistics", "Freight Forwarding", "Customs Brokerage",
    "Supply Chain Finance", "Procurement", "Sourcing", "Vendor Management",
    "Contract Management", "Spend Analysis", "Supplier Relationship Management",
    "Demand Planning", "Forecasting", "Production Planning",
    "Quality Control", "Manufacturing Execution", "Lean Manufacturing",
    "Six Sigma", "Total Quality Management", "Continuous Improvement",
    "Just-in-Time Manufacturing", "Agile Manufacturing", "Flexible Manufacturing",
    "Mass Customization", "Additive Manufacturing", "3D Printing",
    "Robotics Process Automation", "Industrial Internet of Things",
    "Smart Manufacturing", "Digital Twin", "Cyber-Physical Systems",
    "Advanced Manufacturing", "Sustainable Manufacturing",
    "Circular Economy", "Green Manufacturing", "Eco-Design"
]

def generate_startups(n=15):
    prompt = f"""Create {n} fictional startup companies. For each, include:
- name
- industry (from: {', '.join(industries)})
- short description
- estimated valuation (in USD)
- morale score (0–100)
- customers
- a list of 3 dependencies (supply chain)

Return as a Python list of dictionaries.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            temperature=0.7,
            max_tokens=1500
        )

        startup_list = eval(response.choices[0].message["content"])
        return startup_list
    except Exception as e:
        return [{"error": str(e)}]