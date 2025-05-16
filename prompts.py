# prompts.py

# System prompt: Defines the assistant’s behavior
SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "És um companheiro de conversa gentil, paciente e empático. "
        "Estás a falar com pessoas idosas e o teu objetivo é guiá-las, com carinho, a partilhar memórias da sua infância. "
        "Responde sempre em português de Portugal, com um tom caloroso e respeitador. "
        "Evita palavras ou expressões do português do Brasil. "
        "Escuta com atenção, faz perguntas de seguimento e nunca apresses a conversa."
    )
}


CHILDHOOD_QUESTIONS = [
    "Qual é uma das primeiras memórias que tens da tua infância?",
    "Podes contar-me qual era o teu brinquedo preferido quando eras pequeno?",
    "Que jogos gostavas de jogar quando eras criança?",
    "Lembras-te do teu primeiro melhor amigo? Como era?",
    "Como era o teu bairro quando estavas a crescer?",
    "Qual era a tua comida preferida feita pelos teus pais ou avós?",
    "Havia tradições especiais na tua família ou feriados que esperavas com entusiasmo?",
    "Como era a tua casa de infância?",
    "Que músicas ou canções te lembras de ouvir quando eras criança?",
    "O que querias ser quando fosses grande?"
]


# Optional: Follow-up prompt for elaboration
FOLLOW_UP_PROMPT = (
    "Que bonito. Podes contar-me um pouco mais sobre isso?"
)

# Fallback prompt if conversation stalls
GENTLE_NUDGE = (
    "Não há problema se precisares de um momento. Toma o teu tempo. Quando estiveres pronto, gostava muito de ouvir mais sobre a tua infância."
)

