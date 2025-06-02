# styles.py
def get_custom_css():
    return """
    <style>
    /* ======== PALETA ZOMBIE ======== */
    /* #4E5C51 #2E4E4D #491E31 #81454E #AB6F61 #B1A187 */

    /* Fondo general */
    body, .stApp {
        background-color: #2E4E4D;   /* fondo base gris-verdoso */
        color: #B1A187;              /* texto principal */
        font-family: 'Segoe UI', sans-serif;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #B1A187;
    }

    /* ---------- FORMULARIO ---------- */
    div[data-testid="stForm"] {
        background-color: #6E7D6A;   /* panel del form */
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 0 15px rgba(0,0,0,0.35);
    }

    /* Etiquetas de los inputs */
    label {
        font-weight: 600;
        color: #F5F5F5 !important;
    }

    div[data-testid="stTickBarMax"],
    div[data-testid="stTickBarMin"] {
        color: #491E31 !important;
    }


    /* ======== BOTÓN DE FORMULARIO PERSONALIZADO ======== */
    button[kind="secondaryFormSubmit"]:hover {
        background-color: #D3D3D3 !important;  /* gris claro */
        color: #491E31 !important;             /* texto oscuro para buen contraste */
        font-weight: bold !important;
        transition: background-color 0.3s ease !important;
    }

    .stFormSubmitButton button.st-emotion-cache-ktz07o {
        background-color: #81454E !important;
        color: white !important;
    }

    /* ---------- CUADROS DE RESULTADO ---------- */
    .survive-box {
        background-color: #314949;  /* marrón claro (resultado positivo) */
        padding: 20px;
        border-radius: 12px;
        color: #F5F5F5;
        text-align: center;
    }
    .nosurvive-box {
        background-color: #491E31;  /* burdeos oscuro (resultado negativo) */
        padding: 20px;
        border-radius: 12px;
        color: #F5F5F5;
        text-align: center;
    }

    /* Margen general */
    .block-container { padding: 2rem 4rem; }

    </style>
    """