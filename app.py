import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="Simulador de Ondas - PROFESSOR ROBERTO OLIVEIRA",
    layout="wide"
)

# ================= ESTILO ====================

st.markdown("""
<style>

.stApp{
    background-color:#050505;
    color:white;
}

[data-testid="stSidebar"]{
    background:linear-gradient(#0b0b0b,#07122f);
}

[data-testid="stSidebar"] *{
    color:white !important;
}

h1,h2,h3,h4{
    color:#ffbe2e !important;
}

.info-box{
    background:#0f1d45;
    border:1px solid #2e467f;
    border-radius:10px;
    padding:15px;
    color:white;
}

.info-box *{
    color:white !important;
}

.legend{
    background:#111111;
    border:1px solid #444;
    border-radius:10px;
    padding:20px;
    color:white;
}

.legend *{
    color:white !important;
}

</style>
""",unsafe_allow_html=True)

# ================= TÍTULO ====================

st.title("🌊 Simulador de Ondas - PROFESSOR ROBERTO OLIVEIRA")

# ================= SIDEBAR ====================

with st.sidebar:

    st.header("Tipo de onda")

    tipo=st.selectbox(
        "",
        ["Longitudinal","Transversal"]
    )

    amplitude=st.slider(
        "Amplitude",
        1,
        20,
        10
    )

    frequencia=st.slider(
        "Frequência (Hz)",
        1.0,
        5.0,
        2.0
    )

    comprimento=st.slider(
        "Comprimento de onda (λ)",
        10,
        50,
        25
    )

    velocidade=st.slider(
        "Velocidade",
        1,
        10,
        5
    )

    espiras=st.slider(
        "Número de espiras",
        30,
        120,
        80
    )

    iniciar=st.checkbox(
        "▶ Iniciar",
        value=True
    )

    st.markdown("---")

    st.markdown("""

<div class='info-box'>

<h4>Sobre a onda longitudinal</h4>

Nesta onda as partículas vibram na mesma direção da propagação, formando regiões de:

<br>

🔵 Compressão

Espiras mais próximas

<br><br>

🔴 Rarefação

Espiras mais afastadas

</div>

""",unsafe_allow_html=True)

grafico=st.empty()

t=0

# ================= ANIMAÇÃO ====================

while iniciar:

    fig=plt.figure(
        figsize=(14,5),
        facecolor='black'
    )

    ax=fig.add_subplot(111)

    ax.set_facecolor("black")

    x=np.linspace(
        0,
        100,
        4000
    )

    if tipo=="Longitudinal":

        deslocamento=amplitude*np.sin(
            2*np.pi*(
                x/comprimento
                -frequencia*t
            )
        )

        x2=x+deslocamento

        y=3*np.sin(
            2*np.pi*x*(espiras/100)
        )

        ax.plot(
            x2,
            y,
            color="#ffbe2e",
            linewidth=2.5
        )

        # seta

        ax.annotate(
            '',
            xy=(60,7),
            xytext=(35,7),
            arrowprops=dict(
                color='lime',
                width=2
            )
        )

        ax.text(
            38,
            8,
            "Direção de propagação",
            color='lime',
            fontsize=12
        )

        # legendas da onda

        ax.text(
            18,
            -7,
            "Compressão",
            color='dodgerblue',
            fontsize=14,
            fontweight='bold'
        )

        ax.text(
            45,
            -7,
            "Rarefação",
            color='red',
            fontsize=14,
            fontweight='bold'
        )

        ax.text(
            75,
            -7,
            "Compressão",
            color='dodgerblue',
            fontsize=14,
            fontweight='bold'
        )

    else:

        y=amplitude*np.sin(
            2*np.pi*(
                x/comprimento
                -frequencia*t
            )
        )

        ax.plot(
            x,
            y,
            linewidth=3,
            color="#ffbe2e"
        )

        ax.set_title(
            "Onda Transversal",
            color="#ffbe2e",
            fontsize=28
        )

    ax.set_xlim(0,100)
    ax.set_ylim(-10,10)

    ax.set_title(
        f"Onda {tipo}",
        color="#ffbe2e",
        fontsize=28
    )

    ax.grid(alpha=0.15)

    ax.tick_params(
        colors='white'
    )

    for s in ax.spines.values():
        s.set_color("white")

    grafico.pyplot(
        fig,
        clear_figure=True
    )

    # ================= ÁREA INFERIOR =================

    col1,col2=st.columns(2)

    with col1:

        fig2=plt.figure(
            figsize=(7,3),
            facecolor="black"
        )

        ax2=fig2.add_subplot(111)

        ax2.set_facecolor(
            "black"
        )

        y2=np.sin(
            x/3-frequencia*t
        )

        ax2.plot(
            x,
            y2,
            color="#ffbe2e",
            linewidth=2
        )

        ax2.set_title(
            "Gráfico de Densidade",
            color="#ffbe2e"
        )

        ax2.tick_params(
            colors='white'
        )

        for s in ax2.spines.values():
            s.set_color(
                "white"
            )

        st.pyplot(fig2)

    with col2:

        st.markdown("""

<div class='legend'>

<h3>Legenda</h3>

<p style="color:#4da6ff;">
🔵 Compressão
</p>

Espiras mais próximas

<br><br>

<p style="color:red;">
🔴 Rarefação
</p>

Espiras mais afastadas

<br><br>

<p style="color:lime;">
🟢 Direção de propagação
</p>

Sentido em que a onda se move

</div>

""",unsafe_allow_html=True)

    t+=0.05

    time.sleep(0.03)