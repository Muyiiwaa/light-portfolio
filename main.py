import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Portfolio"
PAGE_ICON = ":computer:"
NAME = "TONY OREOLUWA"
DESCRIPTION = """
Experienced Data Analytics expert with a passion for building efficient, state of the art data solutions.
Specialized in data analysis, business intelligence, and database management.
"""
EMAIL = "your.email@example.com"
SOCIAL_MEDIA = {
    "LinkedIn": {
        "link": "http://linkedin.com/in/iyiolaoreoluwa",
        "logo": "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg",
    },
    "GitHub": {
        "link": "https://github.com/",
        "logo": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    },
    "Twitter": {
        "link": "https://twitter.com/",
        "logo": "https://abs.twimg.com/favicons/twitter.3.ico",
    },
}


PROJECTS = {
    "Project 1: Awesome Web App": {
        "description": "A powerful web application built using Python, Streamlit and other awesome frameworks...",
        "link": "https://yourproject1.com",
    },
    "NESTLE AUSTRALIA ANALYSIS DASHBOARD": {
        "description": "A dashboard that provides insights into the Nestle Australia business",
        "link": "https://shorturl.at/zstqk",
    },
    "Project 3: Machine Learning Model": {
        "description": "A sophisticated machine learning model with high prediction accuracy...",
        "link": "https://yourproject3.com",
    },
    "Project 4: Mobile Application": {
        "description": "A mobile application developed for both Android and iOS platforms...",
        "link": "https://yourproject4.com",
    },
}

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- HERO SECTION ---
st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
    label=" 📄 Download My CV",
    data="assets/OREOLUWA_IYIOLA_Resume.pdf",  # Replace with your actual CV content or a path to it
    file_name="OREOLUWA_IYIOLA_Resume.pdf",
    mime="application/octet-stream",  # use application/octet-stream if you are not using a pdf
)

# --- SOCIAL LINKS ---
social_links_html = ""
for platform, details in SOCIAL_MEDIA.items():
    social_links_html += f'<a href="{details["link"]}" target="_blank"><img src="{details["logo"]}" width="30" height="30" alt="{platform}"/></a>'

st.markdown(social_links_html, unsafe_allow_html=True)

st.markdown("---")

# --- PROJECTS SECTION ---
st.header("Projects")

project_items = list(PROJECTS.items())  # Convert to list
num_projects = len(project_items)

if num_projects > 0:  # Ensure that we have at least one project
    cols = st.columns(2)  # Use 2 columns
    for i in range(0, num_projects, 2):  # Iterate through the list with a step of 2
        project1_name, project1_details = project_items[i]
        with cols[0]:  # Put the first project in column 1
            with st.container(height=270, border=True):
                st.subheader(project1_name, divider=True)
                st.write(project1_details["description"])
                if st.button(f"See Project", key=f"project1_{i}"):  # Unique key for each button
                    st.markdown(f'<a href="{project1_details["link"]}" target="_blank"></a>', unsafe_allow_html=True)

        # Check if there is a second project before displaying it
        if i + 1 < num_projects:
            project2_name, project2_details = project_items[i + 1]
            with cols[1]:  # Put the second project in column 2
                with st.container(height=270, border=True):
                    st.subheader(project2_name, divider=True)
                    st.write(project2_details["description"])
                    if st.button(f"See Project", key=f"project2_{i}"):  # Unique key for each button
                        st.markdown(f'<a href="{project2_details["link"]}" target="_blank"></a>', unsafe_allow_html=True)

st.divider()

# --- CONTACT SECTION ---
st.header("Contact Me")
contact_form = """
<form action="https://formsubmit.co/your_formsubmit_id" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)


# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")