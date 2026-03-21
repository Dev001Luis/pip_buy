# Pip-Boy Mobile Replica (Python)

## Overview

This project is my attempt to recreate a **fully functional, accurate replica of the Pip-Boy interface** from the Fallout 4 universe.

The goal is to build a **mobile application written primarily in Python** that reproduces the look, behavior, and interaction model of the iconic Pip-Boy device. The application is designed to run on smartphones and emulate the experience of navigating a Pip-Boy system, including screens such as:

- STAT
- INV
- DATA
- MAP
- RADIO

The project aims to reproduce the **logic and interaction flow** of the original interface while maintaining clean architecture and maintainable code.

This project serves two main purposes:

1. **Technical exploration** of mobile UI development using Python.
2. **Portfolio demonstration** of software architecture, UI replication, and application design.

---

# Goals of the Project

My objectives with this project are:

- Recreate the Pip-Boy interface as faithfully as possible.
- Build a **touch-friendly mobile UI** optimized for smartphones.
- Maintain a **clean and professional project architecture**.
- Separate **logic, UI, and data layers** clearly.
- Package the project as an **installable mobile application**.
- Keep the codebase readable and maintainable.

I also treat this project as a way to explore how far Python can go for **UI-driven mobile applications**.

---

# Technology Stack

The project is built using the following technologies:

### Language

- Python

### UI Framework

- Kivy

### Mobile Packaging

- Buildozer (Android)
- Kivy-iOS (iOS)

### Graphics

- OpenGL (via Kivy)
- Custom fonts and textures

### Audio

- Built-in audio support provided by Kivy

# Why Kivy ?! Why not

**Python-native mobile application** and access to:

- GPU-accelerated rendering
- touch input
- cross-platform compatibility
- custom UI widgets

Kivy provides all of these features while allowing me to stay entirely within the Python ecosystem.

# Project Features

The application will replicate the major Pip-Boy systems.

## STAT

Displays character information such as:

- health
- KCal
- H2O (Idratation)
- character statistics
- status indicators

Possible extensions:

- health animations
- condition diagrams
- animated gauges

---

## INV (Inventory)

Inventory management system.

Features include:

- skills
- knowledge
- equip / unequip system

Possible inventory categories:

- tech languages
- framewors
- softwares

---

## DATA

Quest and information management.

Features:

- quest log (**shopping list ??**)
- objectives
- notes
- system messages

---

## MAP

Map navigation screen.

Planned features:

- location markers
- zooming
- player location indicator
- scrolling map

The map system will be simplified compared to the original games but will replicate the **visual style and navigation model**.

---

## RADIO

Audio playback system.

Features:

- radio station list
- music playback
- play / pause / station switching

---

# Interface Design

The UI is heavily inspired by the visual style of the Pip-Boy interface.

Key characteristics include:

- monochrome green color palette
- retro terminal aesthetic
- pixel-grid UI
- tab-based navigation
- scrolling lists
- animated gauges

The application is designed to emulate the feel of a **retro CRT display**.

---

# Mobile Optimization

Since the application is intended for mobile devices, the interface is designed with the following constraints:

### Touch-friendly navigation

Buttons are designed to be large enough for comfortable touch interaction.

### Landscape orientation

The application will run primarily in **landscape mode** to replicate the horizontal Pip-Boy layout.

### Resolution scaling

The UI is designed around a **base resolution** and then scaled dynamically to match the device screen.

Example base resolution:

480 × 320

This allows the interface to maintain pixel accuracy across devices.

---

# Project Architecture

The project follows a modular structure that separates UI, logic, and assets.

```
pipboy/
│
├── main.py
│
├── app/
│   ├── screens/
│   │   ├── stat_screen.py
│   │   ├── inventory_screen.py
│   │   ├── data_screen.py
│   │   ├── map_screen.py
│   │   └── radio_scr│een.py
│   │
│   ├── themes/
│   │   └── color_palette.py
│   │
│   ├── widgets/
│   │   ├── pipboy_button.py
│   │   ├── gauge_widget.py
│   │   └── list_item_widget.py
│   │
│   ├── core/
│   │   ├── player_stats.py
│   │   ├── inventory_system.py
│   │   ├── quest_log.py
│   │   ├── map_engine.py
│   │   └── radio_player.py
│   │
│   └── assets/
│       ├── fonts/
│       ├── textures/
│       └── sounds/
│
└── README.md
```

### UI Layer

Contains all interface components and screens.

### Core Layer

Contains application logic and data models.

### Assets

Contains all graphical and audio resources.

---

# Development Approach

I follow a staged development process.

## Phase 1 — UI Skeleton

- layout structure
- tab navigation
- empty screens
- font integration
- color palette

Goal: establish the visual structure of the interface.

---

## Phase 2 — Core Systems

Implement application logic:

- player statistics
- inventory system
- quest log

Goal: connect real data to the interface.

---

## Phase 3 — Advanced Systems

Add complex systems:

- map engine
- radio player
- dynamic UI updates

---

## Phase 4 — Visual Polish

Final visual improvements:

- CRT effects
- scanlines
- animations
- audio feedback

---

# Installation (Development)

Clone the repository:

```
git clone https://github.com/yourusername/pipboy-mobile.git
cd pipboy-mobile
```

Install dependencies:

```
pip install kivy
```

Run the application:

```
python main.py
```

---

# Building the Mobile App

To build the Android version, I use Buildozer.

Install Buildozer:

```
pip install buildozer
```

Initialize build configuration:

```
buildozer init
```

Build the Android APK:

```
buildozer android debug
```

The generated APK can then be installed directly on an Android device.

---

# Current Status

This project is currently in development.

The current milestone focuses on building the **UI framework and screen navigation system** before implementing the underlying game systems.

---

# Future Ideas

Possible extensions include:

- real device integration (battery level, GPS, etc.)
- AI
- real-time data widgets
- expanded UI animations
- customizable Pip-Boy themes (we could give like in the real Pip-Boy possibility to modifcy HUD layout by changing in different colours)

---

# Disclaimer

This project is a **fan-made technical experiment** inspired by the Pip-Boy interface from the Fallout series.

All rights to the original Pip-Boy design belong to Fallout Brand.

---

# Author

LuisDev001
Software developer exploring:

- Python
- UI engineering
- mobile application architecture
- game-style interfaces

# Attributions

For music control panel buttons png:
<a href="https://www.flaticon.com/free-icons/music-control" title="music control icons">Music control icons created by nawicon - Flaticon</a>
