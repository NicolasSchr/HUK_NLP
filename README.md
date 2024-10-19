# HUK_NLP
HUK_Coburg_CodingChallenge

# Sentiment Analysis:
Ich hab mich für ein Finetuning von BERT entschieden. Primär weil es mich interessiert hat, wie gut das Funktionieren würde.
Weitere Erklärungen und Beschreibungen finden sich im ersten CodeBlock im Notebook, in den Kommentaren und am Ende.
Ps: Mein Cuda hat zwischendurch auf einmal aufgehört zu funktionieren, weswegen das Training auf Colab gelaufen ist und Inference auf CPU läuft.

Dropbox Link für die model weights: https://www.dropbox.com/scl/fi/s6ui2jafztgtyxvau6pkx/model_low_lr.pth?rlkey=kqopb53lkzky5ca2qz5y0p2en&st=iwa18tvr&dl=0

# Für die RestApi:
- Dockerfile bauen
- Container starten mit "docker run -it -p 5000:5000 predictrestapi:latest"
- Abfrage testen: curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"inputs": ["I really like this. Its awesome"]}'
