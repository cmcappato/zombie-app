def get_custom_css():
    return """
    <style>
    /* Fondo general y texto */
    .main {
        background-color: #2E4E4D !important;
        color: #B1A187 !important;
    }

    /* Botones */
    .stButton>button {
        background-color: #491E31 !important;
        color: #B1A187 !important;
        border-radius: 8px;
        border: none;
        padding: 8px 15px;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #81454E !important;
        color: white !important;
    }

    /* Paneles y contenedores */
    .css-1d391kg, .stForm {
        background-color: #4E5C51 !important;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #AB6F61 !important;
    }

    /* Scrollbars personalizados (opcional) */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #2E4E4D;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #491E31;
        border-radius: 10px;
    }
    </style>
    """
