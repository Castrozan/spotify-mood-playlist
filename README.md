# Spotify Mood Playlist Recommender

This project is a Spotify playlist recommender that suggests playlists based on your mood, which is determined by a combination of color selection and mood parameters.

[try live demo](https://spotify-mood-playlist.onrender.com/)

This project was created with manus @https://manus.im/share/ezuX6i5mgP7iIURDuS9dW7?replay=1

## How It Works

The application uses a three-dimensional mood assessment system to recommend playlists:

1.  **Valence (V)**: Your happiness level.
2.  **Energy (E)**: Your energy level.
3.  **Dominance (D)**: Your sense of control.

You can select from pairs of colors, and optionally fine-tune your mood with sliders for Valence, Energy, and Dominance. These inputs are sent to a proxy server, which then queries the Taranify API to get playlist recommendations tailored to your mood.

## Credit

This project was created with the assistance of an AI pair programmer. The original development session can be viewed at [Manus](https://manus.im/share/ezuX6i5mgP7iIURDuS9dW7?replay=1). 