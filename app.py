import streamlit as st
import json
import os
from datetime import datetime

# ─────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Hospital Management System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0a0f1e; color: #e2e8f0; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1e2d47;
    }

    /* Cards */
    .card {
        background: #151f33;
        border: 1px solid #1e2d47;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
    }

    /* Stat cards */
    .stat-card {
        background: #151f33;
        border: 1px solid #1e2d47;
        border-radius: 12px;
        padding: 20px 24px;
        text-align: center;
    }
    .stat-num {
        font-size: 36px;
        font-weight: 700;
        margin: 0;
    }
    .stat-lbl {
        font-size: 13px;
        color: #94a3b8;
        margin: 0;
    }

    /* Buttons */
    .stButton > button {
        background: #3b82f6;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        padding: 8px 20px;
        width: 100%;
    }
    .stButton > button:hover {
        background: #2563eb;
        color: white;
    }

    /* Input fields */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background: #111827;
        border: 1px solid #1e2d47;
        border-radius: 8px;
        color: #e2e8f0;
    }

    /* Table */
    .stDataFrame { border-radius: 10px; overflow: hidden; }

    /* Success/Error */
    .stSuccess { background: #0f3320; border: 1px solid #22c55e; border-radius: 8px; }
    .stError   { background: #4c1616; border: 1px solid #ef4444; border-radius: 8px; }
    .stInfo    { background: #1d3f6e; border: 1px solid #3b82f6; border-radius: 8px; }
    .stWarning { background: #3d2a07; border: 1px solid #f59e0b; border-radius: 8px; }

    /* Page title */
    .page-title {
        font-size: 26px;
        font-weight: 700;
        color: #e2e8f0;
        margin-bottom: 4px;
    }
    .page-sub {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 24px;
    }

    /* Queue item */
    .queue-item {
        background: #1a2235;
        border: 1px solid #1e2d47;
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 10px;
    }
    .queue-first {
        background: #4c1616;
        border: 1px solid #ef4444;
    }

    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
#  DATA FILES
# ─────────────────────────────────────────
PATIENTS_FILE  = "patients.json"
DOCTORS_FILE   = "doctors.json"
EMERGENCY_FILE = "emergency.json"
BILLS_FILE     = "bills.json"

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return []

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

# ─────────────────────────────────────────
#  SESSION STATE INIT
# ─────────────────────────────────────────
if "patients"  not in st.session_state: st.session_state.patients  = load_data(PATIENTS_FILE)
if "doctors"   not in st.session_state: st.session_state.doctors   = load_data(DOCTORS_FILE)
if "emergency" not in st.session_state: st.session_state.emergency = load_data(EMERGENCY_FILE)
if "bills"     not in st.session_state: st.session_state.bills     = load_data(BILLS_FILE)

# ─────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏥 Hospital MS")
    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["📊 Dashboard", "🧑‍⚕️ Patients", "👨‍⚕️ Doctors", "🚨 Emergency", "💳 Billing"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("**System Stats**")
    st.markdown(f"🧑‍⚕️ Patients: **{len(st.session_state.patients)}**")
    st.markdown(f"👨‍⚕️ Doctors: **{len(st.session_state.doctors)}**")
    st.markdown(f"🚨 Emergency Queue: **{len(st.session_state.emergency)}**")
    st.markdown(f"💳 Bills Generated: **{len(st.session_state.bills)}**")

    st.markdown("---")
    if st.button("💾 Save All Data"):
        save_data(PATIENTS_FILE,  st.session_state.patients)
        save_data(DOCTORS_FILE,   st.session_state.doctors)
        save_data(EMERGENCY_FILE, st.session_state.emergency)
        save_data(BILLS_FILE,     st.session_state.bills)
        st.success("All data saved!")

# ─────────────────────────────────────────
#  DASHBOARD
# ─────────────────────────────────────────
if page == "📊 Dashboard":
    st.markdown('<div class="page-title">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Overview of all hospital operations</div>', unsafe_allow_html=True)

    # Stat cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-num" style="color:#3b82f6">{len(st.session_state.patients)}</p>
            <p class="stat-lbl">Total Patients</p>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-num" style="color:#14b8a6">{len(st.session_state.doctors)}</p>
            <p class="stat-lbl">Total Doctors</p>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-num" style="color:#ef4444">{len(st.session_state.emergency)}</p>
            <p class="stat-lbl">Emergency Queue</p>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="stat-card">
            <p class="stat-num" style="color:#22c55e">{len(st.session_state.bills)}</p>
            <p class="stat-lbl">Bills Generated</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧑‍⚕️ Recent Patients")
        if st.session_state.patients:
            for p in st.session_state.patients[-3:][::-1]:
                st.markdown(f"""
                <div class="queue-item">
                    <strong>{p['name']}</strong>
                    <span style="color:#94a3b8; font-size:13px"> — {p['disease']}</span><br>
                    <span style="color:#3b82f6; font-size:12px">ID: {p['id']} | Age: {p['age']}</span>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("No patients registered yet.")

    with col2:
        st.markdown("### 👨‍⚕️ Recent Doctors")
        if st.session_state.doctors:
            for d in st.session_state.doctors[-3:][::-1]:
                st.markdown(f"""
                <div class="queue-item">
                    <strong>Dr. {d['name']}</strong>
                    <span style="color:#94a3b8; font-size:13px"> — {d['spec']}</span><br>
                    <span style="color:#14b8a6; font-size:12px">ID: {d['id']} | Age: {d['age']}</span>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("No doctors registered yet.")

# ─────────────────────────────────────────
#  PATIENTS
# ─────────────────────────────────────────
elif page == "🧑‍⚕️ Patients":
    st.markdown('<div class="page-title">🧑‍⚕️ Patient Management</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Register and manage all patients</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("### ➕ Add New Patient")
        with st.form("add_patient_form", clear_on_submit=True):
            pid     = st.number_input("Patient ID",  min_value=1, step=1)
            pname   = st.text_input("Full Name",     placeholder="e.g. Ahmed Ali")
            page_   = st.number_input("Age",         min_value=0, max_value=150, step=1)
            pdisease= st.text_input("Disease",       placeholder="e.g. Hypertension")
            submitted = st.form_submit_button("✚ Add Patient")

            if submitted:
                if not pname or not pdisease:
                    st.error("Please fill all fields!")
                elif any(p['id'] == pid for p in st.session_state.patients):
                    st.error(f"Patient ID {pid} already exists!")
                else:
                    st.session_state.patients.append({
                        "id": pid, "name": pname,
                        "age": page_, "disease": pdisease
                    })
                    save_data(PATIENTS_FILE, st.session_state.patients)
                    st.success(f"Patient '{pname}' added successfully!")
                    st.rerun()

    with col2:
        st.markdown("### 📋 All Patients")
        if st.session_state.patients:
            for p in st.session_state.patients:
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"""
                    <div class="queue-item">
                        <strong>{p['name']}</strong>
                        <span style="color:#3b82f6; font-size:12px; margin-left:10px">#{p['id']}</span><br>
                        <span style="color:#94a3b8; font-size:13px">Age: {p['age']} | 🦠 {p['disease']}</span>
                    </div>""", unsafe_allow_html=True)
                with c2:
                    if st.button("🗑", key=f"del_p_{p['id']}"):
                        st.session_state.patients = [x for x in st.session_state.patients if x['id'] != p['id']]
                        save_data(PATIENTS_FILE, st.session_state.patients)
                        st.rerun()
        else:
            st.info("No patients registered yet.")

# ─────────────────────────────────────────
#  DOCTORS
# ─────────────────────────────────────────
elif page == "👨‍⚕️ Doctors":
    st.markdown('<div class="page-title">👨‍⚕️ Doctor Management</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Register and manage all doctors</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("### ➕ Add New Doctor")
        with st.form("add_doctor_form", clear_on_submit=True):
            did   = st.number_input("Doctor ID",       min_value=1, step=1)
            dname = st.text_input("Full Name",         placeholder="e.g. Dr. Sarah Khan")
            dage  = st.number_input("Age",             min_value=0, max_value=100, step=1)
            dspec = st.text_input("Specialization",    placeholder="e.g. Cardiology")
            submitted = st.form_submit_button("✚ Add Doctor")

            if submitted:
                if not dname or not dspec:
                    st.error("Please fill all fields!")
                elif any(d['id'] == did for d in st.session_state.doctors):
                    st.error(f"Doctor ID {did} already exists!")
                else:
                    st.session_state.doctors.append({
                        "id": did, "name": dname,
                        "age": dage, "spec": dspec
                    })
                    save_data(DOCTORS_FILE, st.session_state.doctors)
                    st.success(f"Dr. '{dname}' added successfully!")
                    st.rerun()

    with col2:
        st.markdown("### 📋 All Doctors")
        if st.session_state.doctors:
            for d in st.session_state.doctors:
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"""
                    <div class="queue-item">
                        <strong>Dr. {d['name']}</strong>
                        <span style="color:#14b8a6; font-size:12px; margin-left:10px">#{d['id']}</span><br>
                        <span style="color:#94a3b8; font-size:13px">Age: {d['age']} | 🩺 {d['spec']}</span>
                    </div>""", unsafe_allow_html=True)
                with c2:
                    if st.button("🗑", key=f"del_d_{d['id']}"):
                        st.session_state.doctors = [x for x in st.session_state.doctors if x['id'] != d['id']]
                        save_data(DOCTORS_FILE, st.session_state.doctors)
                        st.rerun()
        else:
            st.info("No doctors registered yet.")

# ─────────────────────────────────────────
#  EMERGENCY
# ─────────────────────────────────────────
elif page == "🚨 Emergency":
    st.markdown('<div class="page-title">🚨 Emergency Queue</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">FIFO priority queue — first in, first processed</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.markdown("### ➕ Add Emergency Patient")
        with st.form("add_emergency_form", clear_on_submit=True):
            eid      = st.number_input("Patient ID",  min_value=1, step=1)
            ename    = st.text_input("Full Name",     placeholder="e.g. Usman Raza")
            eage     = st.number_input("Age",         min_value=0, max_value=150, step=1)
            edisease = st.text_input("Condition",     placeholder="e.g. Cardiac Arrest")
            submitted = st.form_submit_button("🚨 Add to Queue")

            if submitted:
                if not ename or not edisease:
                    st.error("Please fill all fields!")
                else:
                    st.session_state.emergency.append({
                        "id": eid, "name": ename,
                        "age": eage, "disease": edisease,
                        "time": datetime.now().strftime("%H:%M:%S")
                    })
                    save_data(EMERGENCY_FILE, st.session_state.emergency)
                    st.success(f"'{ename}' added to emergency queue!")
                    st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### ⚡ Process Next")
        st.markdown(f"**{len(st.session_state.emergency)}** patient(s) in queue")

        if st.button("▶ Process Next Patient", type="primary"):
            if st.session_state.emergency:
                processed = st.session_state.emergency.pop(0)
                save_data(EMERGENCY_FILE, st.session_state.emergency)
                st.success(f"✅ Processed: **{processed['name']}** — {processed['disease']}")
                st.rerun()
            else:
                st.error("No emergency patients in queue!")

    with col2:
        st.markdown("### 🚑 Current Queue")
        if st.session_state.emergency:
            for i, p in enumerate(st.session_state.emergency):
                style = "queue-first" if i == 0 else ""
                label = "🔴 NEXT" if i == 0 else f"#{i+1}"
                st.markdown(f"""
                <div class="queue-item {style}">
                    <span style="font-weight:700">{label} — {p['name']}</span><br>
                    <span style="color:#94a3b8; font-size:13px">
                        ID: {p['id']} | Age: {p['age']} | {p['disease']}
                    </span>
                    <span style="color:#94a3b8; font-size:11px; float:right">
                        Added: {p.get('time','N/A')}
                    </span>
                </div>""", unsafe_allow_html=True)
        else:
            st.success("✅ No emergency patients in queue!")

# ─────────────────────────────────────────
#  BILLING
# ─────────────────────────────────────────
elif page == "💳 Billing":
    st.markdown('<div class="page-title">💳 Billing</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">Generate bills based on service type</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Select Bill Type")

        bill_type = st.radio(
            "Bill Type",
            ["🏥 General Bill — Rs. 500", "🚨 Emergency Bill — Rs. 1500"],
            label_visibility="collapsed"
        )

        amount = 500 if "General" in bill_type else 1500
        label  = "General Consultation" if "General" in bill_type else "Emergency Services"

        st.markdown(f"""
        <div class="stat-card" style="margin:16px 0">
            <p class="stat-num" style="color:{'#22c55e' if amount==500 else '#ef4444'}">
                Rs. {amount}
            </p>
            <p class="stat-lbl">{label}</p>
        </div>""", unsafe_allow_html=True)

        if st.button("💳 Generate Bill"):
            st.session_state.bills.append({
                "type": label,
                "amount": amount,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            save_data(BILLS_FILE, st.session_state.bills)
            st.success(f"✅ Bill generated: **Rs. {amount}** for {label}")
            st.rerun()

    with col2:
        st.markdown("### 🧾 Bill History")
        if st.session_state.bills:
            total = sum(b['amount'] for b in st.session_state.bills)
            st.markdown(f"""
            <div class="stat-card" style="margin-bottom:16px">
                <p class="stat-num" style="color:#22c55e">Rs. {total}</p>
                <p class="stat-lbl">Total Revenue ({len(st.session_state.bills)} bills)</p>
            </div>""", unsafe_allow_html=True)

            for b in st.session_state.bills[-5:][::-1]:
                color = "#22c55e" if b['amount'] == 500 else "#ef4444"
                st.markdown(f"""
                <div class="queue-item" style="display:flex;justify-content:space-between;align-items:center">
                    <div>
                        <strong>{b['type']}</strong><br>
                        <span style="color:#94a3b8;font-size:12px">{b['time']}</span>
                    </div>
                    <strong style="color:{color}">Rs. {b['amount']}</strong>
                </div>""", unsafe_allow_html=True)
        else:
            st.info("No bills generated yet.")
