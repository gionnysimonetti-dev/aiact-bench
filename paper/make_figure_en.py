"""English version of figure 1 (declared confidence vs fully correct answers)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
for f in ["/usr/share/fonts/truetype/google-fonts/Inter-Regular.ttf", "/usr/share/fonts/truetype/google-fonts/Inter[opsz,wght].ttf"]:
    try: fm.fontManager.addfont(f)
    except Exception: pass
plt.rcParams.update({"font.family": ["Inter", "DejaVu Sans"], "font.size": 12, "pdf.fonttype": 42})
ms, conf, acc = ["Claude", "ChatGPT", "Gemini"], [88, 99, 99], [93, 73, 47]
fig, ax = plt.subplots(figsize=(8.5, 4.8))
x, w = range(3), .36
ax.bar([i - w/2 for i in x], conf, w, color="#9CA6B1", label="Mean declared confidence")
ax.bar([i + w/2 for i in x], acc, w, color="#203761", label="Fully correct answers (%)")
for i, (c, a) in enumerate(zip(conf, acc)):
    ax.text(i - w/2, c + 1.2, str(c), ha="center", fontsize=11)
    ax.text(i + w/2, a + 1.2, str(a), ha="center", fontsize=11)
ax.set_xticks(list(x)); ax.set_xticklabels(ms, fontsize=13); ax.set_ylim(0, 112)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="upper center", bbox_to_anchor=(.5, 1.1), ncol=2, frameon=False)
fig.tight_layout(); fig.savefig("fig1_confidence_vs_correctness.pdf"); fig.savefig("fig1_confidence_vs_correctness.png", dpi=150)
