# inputs_layout.py

import streamlit as st
from funcoes_auxiliares import *


def render_inputs(cols, language_key, REATIVOS_DEFAULT, INDUTOR_DEFAULT, nr_bancos, text):
    Q_3f = np.zeros(nr_bancos)
    comp_cabo = np.zeros(nr_bancos)
    comp_barra = np.zeros(nr_bancos)
    L_unit_cabo = np.zeros(nr_bancos)
    L_unit_barra = np.zeros(nr_bancos)
    L_capacitor = np.zeros(nr_bancos)
    L_reator = np.zeros(nr_bancos)

    # Bank #0 (to be energized)
    ii = 0
    k = 0
    with cols[ii]:
        Q_3f_MVAr = st.number_input(
            "$Q_{3\\varphi}$[MVAr] ",
            value=REATIVOS_DEFAULT,
            key="Q_3f_" + str(k),
        )
        Q_3f[k] = Q_3f_MVAr * 1e6  # MVAr -> VAr

    ii = ii + 1
    with cols[ii]:
        comp_cabo_m = st.number_input(
            "$\\ell_{\\rm cable}{\\rm [m]}$",
            value=0.0,
            key="comp_cabo" + str(k),
        )
        comp_cabo[k] = comp_cabo_m

    ii = ii + 1
    with cols[ii]:
        L_unit_cabo_uH_per_m = st.number_input(
            "$L'_{\\rm cable} {\\rm \\left[{\\mu H}/{m} \\right]}$",
            value=0.00,
            key="L_unit_cabo" + str(k),
        )
        L_unit_cabo[k] = L_unit_cabo_uH_per_m * 1e-6  # µH/m -> H/m

    ii = ii + 1
    with cols[ii]:
        L_capacitor_uH = st.number_input(
            "$L_{\\rm capacitor} {\\rm \\left[{\\mu H} \\right]}$",
            value=5.00,
            key="L_capacitor" + str(k),
        )
        L_capacitor[k] = L_capacitor_uH * 1e-6  # µH -> H

    ii = ii + 1
    with cols[ii]:
        L_reator_uH = st.number_input(
            "$L_{\\rm reactor} {\\rm \\left[{\\mu H} \\right]}$",
            value=INDUTOR_DEFAULT,
            key="L_reator" + str(k),
        )
        L_reator[k] = L_reator_uH * 1e-6  # µH -> H

    # Remaining banks (#1 to #n)
    st.markdown(text["already_energized_banks"])
    cols = st.columns(5)
    for k in range(1, nr_bancos):
        ii = 0
        with cols[ii]:
            Q_3f_MVAr = st.number_input(
                "$Q_{3\\varphi}$[MVAr]",
                value=REATIVOS_DEFAULT,
                key="Q_3f_" + str(k),
                label_visibility="visible" if k == 1 else "collapsed",
            )
            Q_3f[k] = Q_3f_MVAr * 1e6

        ii = ii + 1
        with cols[ii]:
            comp_cabo_m = st.number_input(
                "$\\ell_{\\rm cable}{\\rm [m]}$",
                value=0.0,
                key="comp_cabo" + str(k),
                label_visibility="visible" if k == 1 else "collapsed",
            )
            comp_cabo[k] = comp_cabo_m

        ii = ii + 1
        with cols[ii]:
            L_unit_cabo_uH_per_m = st.number_input(
                "$L'_{\\rm cable} {\\rm \\left[{\\mu H}/{m} \\right]}$",
                value=0.00,
                key="L_unit_cabo" + str(k),
                label_visibility="visible" if k == 1 else "collapsed",
            )
            L_unit_cabo[k] = L_unit_cabo_uH_per_m * 1e-6

        ii = ii + 1
        with cols[ii]:
            L_capacitor_uH = st.number_input(
                "$L_{\\rm capacitor} {\\rm \\left[{\\mu H} \\right]}$",
                value=5.00,
                key="L_capacitor" + str(k),
                label_visibility="visible" if k == 1 else "collapsed",
            )
            L_capacitor[k] = L_capacitor_uH * 1e-6

        ii = ii + 1
        with cols[ii]:
            L_reator_uH = st.number_input(
                "$L_{\\rm reactor} {\\rm \\left[{\\mu H} \\right]}$",
                value=INDUTOR_DEFAULT,
                key="L_reator" + str(k),
                label_visibility="visible" if k == 1 else "collapsed",
            )
            L_reator[k] = L_reator_uH * 1e-6

    return Q_3f, comp_cabo, L_unit_cabo, L_capacitor, L_reator



def render_bibliography(text):
    col_bib1, col_bib2 = st.columns([1, 25])

    with col_bib1:
        st.markdown(
            """
            [[1]](https://ieeexplore.ieee.org/document/7035261)\\
            \\
            \\
            [[2]](https://ieeexplore.ieee.org/document/9574631)\\
            \\
            [[3]](https://webstore.iec.ch/publication/62785)\\
            \\
            [[4]](https://ieeexplore.ieee.org/document/5318709)\\
            \\
            \\
            [[5]](https://cdn.standards.iteh.ai/samples/101972/4e7e06bd66d2443da668b8e0c6c60512/IEC-62271-100-2021.pdf)\\
            \\
            [[6]](https://www.normas.com.br/autorizar/visualizacao-nbr/313/identificar/visitante)
            """
        )

    with col_bib2:
        st.markdown(
            """
            IEEE Application Guide for Capacitance Current Switching for AC High-Voltage Circuit Breakers Rated on a Symmetrical Current Basis, in ANSI/IEEE C37.012-1979 , vol., no., pp.1-54, 6 Feb. 1979, doi: 10.1109/IEEESTD.1979.7035261.\\
            IEEE Approved Draft Standard Requirements for Capacitor Switches for AC Systems (1 kV to 38 kV), in IEEE PC37.66/D10, October 2021 , vol., no., pp.1-35, 13 Dec. 2021.\\
            IEC 62271-100 High-voltage switchgear and controlgear - Part 100: Alternating-current circuit-breakers\\
            IEEE Standard for AC High-Voltage Circuit Breakers Rated on a Symmetrical Current Basis--Preferred Ratings and Related Required Capabilities for Voltages Above 1000 V, in IEEE Std C37.06-2009 , vol., no., pp.1-56, 6 Nov. 2009, doi: 10.1109/IEEESTD.2009.5318709.\\
            IEC 62271-100 High-voltage switchgear and controlgear – Part 100: Alternating-current circuit-breakers\\
            NBR 5282 Capacitores de potência em derivação para sistema de tensão nominal acima de 1000 V
            """
        )
