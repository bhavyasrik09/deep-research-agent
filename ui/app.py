import sys
import os
from io import BytesIO

import streamlit as st
from fpdf import FPDF

# -------------------------------------------------
# Path setup
# -------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from main import build_graph

# -------------------------------------------------
# Streamlit UI
# -------------------------------------------------
st.set_page_config(page_title="Deep Research Agent", layout="wide")

st.title("🧠 Deep Research Agent")
st.caption("Multi-agent research system with critic-driven iteration")

topic = st.text_input(
    "Enter a research topic",
    placeholder="e.g. AI agents in healthcare"
)

run = st.button("🚀 Run Research")

# -------------------------------------------------
# Run research
# -------------------------------------------------
if run and topic:
    with st.spinner("Running agents..."):
        try:
            app = build_graph()
            result = app.invoke({
                "topic": topic,
                "plan": [],
                "notes": [],
                "report": "",
                "reports": [],
                "sources": [],
                "critique": "",
                "needs_improvement": True,
                "iteration": 1
            })
        except Exception as e:
            st.error(f"❌ Research failed: {e}")
            result = {
                "report": "No report generated.",
                "reports": [],
                "sources": [],
                "critique": "No critique generated."
            }

    st.success("✅ Research completed!")

    # -------------------------------------------------
    # Display reports
    # -------------------------------------------------
    st.subheader("📄 Report Timeline")

    reports = result.get("reports", [])
    report_text = ""

    if reports:
        for r in reports:
            st.markdown(f"### Iteration {r['iteration']}")
            st.markdown(r.get("report", ""))

            report_text += f"### Iteration {r['iteration']}\n"
            report_text += f"{r.get('report', '')}\n"

            if r.get("sources"):
                st.markdown("**Sources:**")
                report_text += "**Sources:**\n"
                for src in r["sources"]:
                    st.markdown(f"- {src}")
                    report_text += f"- {src}\n"

            st.markdown("---")
    else:
        st.markdown(result.get("report", "No report generated."))
        report_text = result.get("report", "")

    # -------------------------------------------------
    # Critique
    # -------------------------------------------------
    st.subheader("🧐 Critique")
    st.markdown(result.get("critique", "No critique generated."))

    # -------------------------------------------------
    # Export options
    # -------------------------------------------------
    st.subheader("💾 Export Report")

    # -------- Markdown
    st.download_button(
        "📄 Download Markdown",
        data=report_text.encode("utf-8"),
        file_name=f"{topic.replace(' ', '_')}_report.md",
        mime="text/markdown"
    )

    # -------- PDF (UTF-8 safe)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    FONT_PATH = os.path.join(
        os.path.dirname(__file__),
        "fonts",
        "DejaVuSans.ttf"
    )

    if not os.path.exists(FONT_PATH):
        st.error(f"❌ Font file not found: {FONT_PATH}")
    else:
        pdf.add_font("DejaVu", "", FONT_PATH, uni=True)
        pdf.set_font("DejaVu", "", 12)

        for line in report_text.split("\n"):
            pdf.multi_cell(0, 6, line)

        pdf_bytes = BytesIO(pdf.output(dest="S").encode("latin1"))
        pdf_bytes.seek(0)

        st.download_button(
            "📄 Download PDF",
            data=pdf_bytes,
            file_name=f"{topic.replace(' ', '_')}_report.pdf",
            mime="application/pdf"
        )
