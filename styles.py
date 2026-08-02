CUSTOM_CSS = """
<style>

/*====================================================
GOOGLE FONT
====================================================*/

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/*====================================================
MAIN PAGE
====================================================*/

.stApp{

    background:
    linear-gradient(
        135deg,
        #EEF8FF 0%,
        #FFFFFF 45%,
        #FFF9E8 100%
    );

}

/*====================================================
PAGE WIDTH
====================================================*/

.block-container{

    max-width:1300px;

    padding-top:2.5rem;

    padding-bottom:3rem;

    padding-left:2rem;

    padding-right:2rem;

}

/*====================================================
HIDE STREAMLIT
====================================================*/

#MainMenu,
footer,
header{

    visibility:hidden;

}

/*====================================================
SIDEBAR
====================================================*/

section[data-testid="stSidebar"]{

    background:#F9FBFF;

    border-right:1px solid #E5E7EB;

}

/*====================================================
HEADINGS
====================================================*/

h1{

    color:#0F172A !important;

    font-size:34px !important;

    font-weight:700 !important;

    margin-bottom:8px;

}

h2{

    color:#1E293B !important;

    font-size:24px !important;

    font-weight:600;

}

h3{

    color:#334155 !important;

    font-size:18px !important;

    font-weight:600;

}

h4,h5,h6{

    color:#475569 !important;

}

/*====================================================
TEXT
====================================================*/

p,
label{

    color:#475569 !important;

    font-size:15px !important;

}

/*====================================================
AI REVIEW MARKDOWN
====================================================*/

.stMarkdown{

    font-size:15px !important;

    line-height:1.8;

}

.stMarkdown h1{

    font-size:24px !important;

    color:#0F172A !important;

}

.stMarkdown h2{

    font-size:20px !important;

    color:#1E293B !important;

}

.stMarkdown h3{

    font-size:17px !important;

    color:#334155 !important;

}

.stMarkdown strong{

    color:#0F172A !important;

}

.stMarkdown li{

    color:#334155 !important;

    margin-bottom:6px;

}

/*====================================================
BUTTON
====================================================*/

.stButton>button{

    width:100%;

    height:50px;

    border:none;

    border-radius:12px;

    background:
    linear-gradient(
        90deg,
        #7CCBFF,
        #FFD97A
    );

    color:#0F172A;

    font-size:16px;

    font-weight:700;

    transition:.25s;

    box-shadow:
    0 8px 20px rgba(0,0,0,.08);

}

.stButton>button:hover{

    transform:translateY(-2px);

    box-shadow:
    0 12px 25px rgba(0,0,0,.15);

}

/*====================================================
TEXT INPUT
====================================================*/

.stTextInput input{

    background:white;

    color:#0F172A;

    border-radius:12px;

    border:1px solid #CBD5E1;

    padding:10px;

}

.stTextInput input:focus{

    border-color:#38BDF8;

    box-shadow:
    0 0 0 3px rgba(56,189,248,.15);

}

/*====================================================
SELECTBOX
====================================================*/

.stSelectbox div[data-baseweb="select"]{

    background:white;

    border-radius:12px;

    border:1px solid #CBD5E1;

}

div[data-testid="stSelectboxVirtualDropdown"] *{

    background:white !important;

    color:#0F172A !important;

}

/*====================================================
METRIC CARDS
====================================================*/

div[data-testid="stMetric"]{

    background:white;

    border-radius:16px;

    border:1px solid #E5E7EB;

    padding:18px;

    box-shadow:
    0 10px 25px rgba(15,23,42,.08);

    transition:.25s;

}

div[data-testid="stMetric"]:hover{

    transform:translateY(-4px);

}

/*====================================================
EXPANDERS
====================================================*/

div[data-testid="stExpander"]{

    background:white;

    border-radius:14px;

    border:1px solid #E2E8F0;

    margin-bottom:18px;

    box-shadow:
    0 8px 20px rgba(0,0,0,.04);

}

div[data-testid="stExpanderHeader"]{

    color:#0F172A;

    font-size:16px;

    font-weight:600;

}

/*====================================================
TABS
====================================================*/

button[data-baseweb="tab"]{

    background:#F8FAFC;

    color:#475569;

    border-radius:8px;

    font-size:14px;

    font-weight:600;

    margin-right:8px;

}

button[data-baseweb="tab"][aria-selected="true"]{

    background:#38BDF8;

    color:white;

}

/*====================================================
CODE
====================================================*/

pre{

    background:#F1F5F9 !important;

    border-radius:12px;

    border:1px solid #CBD5E1;

}

code{

    color:#0F172A !important;

}

/*====================================================
SUCCESS / INFO / ERROR
====================================================*/

.stSuccess,
.stInfo,
.stError{

    border-radius:12px;

}

/*====================================================
DIVIDER
====================================================*/

hr{

    border:none;

    height:1px;

    background:#E2E8F0;

}

/*====================================================
SCROLLBAR
====================================================*/

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#38BDF8;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:#F8FAFC;

}

</style>
"""