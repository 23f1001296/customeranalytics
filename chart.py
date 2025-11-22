import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Seaborn Professional Styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Synthetic Data Generation ---
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Realistic response-time distributions (minutes)
data = {
    "channel": np.repeat(channels, 250),
    "response_time": np.concatenate([
        np.random.normal(180, 40, 250),   # Email: slower
        np.random.normal(45, 15, 250),    # Chat: fast
        np.random.normal(30, 10, 250),    # Phone: fastest
        np.random.normal(120, 25, 250)    # Social Media: moderate
    ])
}

df = pd.DataFrame(data)

# Ensure all values are positive
df["response_time"] = df["response_time"].clip(lower=1)

# --- Create 512x512 Figure ---
plt.figure(figsize=(8, 8), dpi=64, frameon=False)

sns.violinplot(
    data=df,
    x="channel",
    y="response_time",
    palette="Set2",
    cut=0
)

plt.title("Customer Support Response Time Distribution by Channel")
plt.xlabel("Support Channel")
plt.ylabel("Response Time (minutes)")

plt.gca().set_position([0, 0, 1, 1])  # remove all margins
plt.savefig("chart.png", dpi=64, bbox_inches="tight", pad_inches=0)
plt.close()

