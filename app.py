import streamlit as st
from github_api import get_pr_files
from ai_reviewer import review_patch, summarize_pr
from utils import parse_pr_url
from styles import CUSTOM_CSS

st.set_page_config(
    page_title="AI Github Reviewer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


st.sidebar.success("🟢 Ready")
st.sidebar.divider()
st.sidebar.markdown("""
    ### Tech Stack
    
    - 🐍 Python
    - 🌐 Streamlit
    - 🤖 Groq API
    - 📂 GitHub API
""")


st.markdown("""
<div style="
background:linear-gradient(135deg,#EAF6FF,#FFF7E6);
padding:40px;
border-radius:20px;
box-shadow:0 8px 25px rgba(0,0,0,0.08);
margin-bottom:30px;
">

<h1 style="
margin:0;
color:#0F172A;
font-size:42px;
font-weight:700;
">
🤖 AI GitHub PR Reviewer
</h1>

<p style="
margin-top:12px;
font-size:20px;
color:#475569;
">
Review GitHub Pull Requests with AI-powered insights,
bug detection, security analysis and performance suggestions.
</p>

</div>
""", unsafe_allow_html=True)

left, center, right = st.columns([1, 3, 1])

with center:

    pr_url = st.text_input(
        "🔗 GitHub Pull Request URL",
        placeholder="https://github.com/owner/repo/pull/123"
    )

    user_choice = st.selectbox(
        "🤖 AI Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "meta-llama/llama-prompt-guard-2-86m",
        ]
    )

    review_clicked = st.button(
        "🚀 Analyze Pull Request",
        use_container_width=True
    )

report = ""
repo = ""
pr = ""

if review_clicked:
    if not pr_url:
        st.error("Please enter a Github PR url")
    else:
        try:
            owner, repo, pr = parse_pr_url(pr_url)
            files = get_pr_files(owner, repo, pr)
        except Exception as e:
            st.error(f"❌ {e}")
            st.stop()


        st.toast("✅ Pull Request Loaded")

        reviewable_files = [
            f for f in files
            if "patch" in f and f["filename"].endswith((".py", ".java", ".js", ".cpp", ".c"))
        ]
        st.info(f"📄 Reviewing {len(reviewable_files)} code files")

        if not reviewable_files:
            st.warning("No reviewable source code files found.")
            st.stop()

        all_reviews = []

        progress = st.progress(0)

        report = "# AI Github PR Review\n\n"

        for i, file in enumerate(reviewable_files):
            progress.progress((i + 1) / len(files))

            st.divider()

            with st.spinner(f"🤖 Reviewing {file['filename']}..."):
                try:
                    review = review_patch(
                        file["filename"],
                        file["patch"][:1500],
                        user_choice
                    )
                except Exception as e:
                    st.error(f"Error reviewing {file['filename']}")
                    st.write(e)
                    continue


            all_reviews.append(review)
            report += f"## {file['filename']}\n\n"
            report += review
            report += "\n\n ------------ \n\n"
            with st.expander(f"📄 {file['filename']}", expanded=False):
                tab1, tab2 = st.tabs(["💻 Code", "🤖 AI Review"])
                with tab1:
                    st.code(file["patch"], language="python")
                with tab2:
                    st.markdown(review)

        summary = summarize_pr(
            "\n\n".join(all_reviews),
            user_choice
        )

        st.divider()

        st.header("📊 Overall Pull Request Review")

        st.markdown(summary)

        report += "## Overall Summary\n\n"
        report += summary

        col1, col2, col3 = st.columns(3)
        col1.metric(
            "📄 Files Reviewed",
            len(reviewable_files)
        )

        col2.metric(
            "🤖 Model",
            user_choice
        )

        col3.metric(
            "📥 Report",
            "Ready"
        )



    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name=f"{repo}_PR_{pr}_review.md",
        mime="text/markdown"
    )
    st.toast("🎉 Review completed!")

    st.divider()

    st.markdown("""
    <div style="text-align:center; color:#64748B; padding:20px;">

    Built using Python, Streamlit, Groq & GitHub API

    <br><br>

    © 2026 Mohan Krishna

    </div>
    """, unsafe_allow_html=True)


