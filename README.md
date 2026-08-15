☕ Coffee Shop CLI

A colorful, menu-driven Coffee Shop ordering system built entirely in Python for the terminal.
Browse a 13-item coffee menu, build a cart, review your order, and check out — all wrapped in ANSI colors for a friendlier CLI experience.

---

✨ Features

- 🎨 Colorized terminal output using ANSI escape codes (headers, prices, warnings, and confirmations all stand out)
- 📋 13-item coffee menu, from Espresso to Turkish Coffee
- 🛒 Simple cart system — add items, view your order, and see a running total
- ✅ Checkout confirmation flow so orders aren't placed by accident
- 🔁 Persistent loop — keep ordering until you're ready to exit
- 🧱 Clean, object-oriented structure (`Coffee`, `Order`, and `Colors` classes)

---

📦 Requirements

- Python 3.6+
- No external dependencies — uses only the Python standard library

> 💡 ANSI colors display correctly on most Linux/macOS terminals and modern Windows terminals (Windows Terminal, VS Code terminal). Older `cmd.exe` windows may show raw escape codes instead of colors.

---

🚀 Getting Started

1. Clone the repository

   ```bash
   git clone https://github.com/<your-username>/coffee-shop-cli.git
   cd coffee-shop-cli
   ```

2. Run the app

   ```bash
   python3 coffee_shop.py
   ```

That's it — no `pip install` required.

---

☕ Menu

| # | Coffee | Price |
|---|--------|-------|
| 1 | Espresso | $2.50 |
| 2 | Americano | $3.00 |
| 3 | Latte | $3.50 |
| 4 | Cappuccino | $3.75 |
| 5 | Mocha | $4.00 |
| 6 | Flat White | $3.25 |
| 7 | Macchiato | $3.00 |
| 8 | Affogato | $4.50 |
| 9 | Cold Brew | $3.75 |
| 10 | Vietnamese Coffee | $3.00 |
| 11 | Iced Coffee | $3.50 |
| 12 | Irish Coffee | $4.25 |
| 13 | Turkish Coffee | $2.75 |

---

🕹️ Usage

When you run the app, you'll see the menu along with three extra options:

```
14. View your order
15. Checkout
16. Exit
```

- Enter a number from **1–13** to add that coffee to your cart
- Enter **14** to view your current cart and running total
- Enter **15** to checkout — you'll be asked to confirm before the order is placed
- Enter **16** to exit the program

Example session:

```
..........Welcome to the Coffee Shop..........
1. Espresso - $2.50
2. Americano - $3.00
...
14. View your order
15. Checkout
16. Exit
Choose an option (1-16): 3
Added Latte to your cart!

Choose an option (1-16): 14

Your Orders:
1. Latte - $3.50
Total: $3.50

Choose an option (1-16): 15
Process your checkout? (yes/no): yes
Checkout completed. Enjoy your coffee!
```

---

🏗️ Project Structure

```
coffee_shop.py
├── Colors        # ANSI color code constants for styled output
├── Coffee         # Represents a single menu item (name + price)
├── Order          # Manages the cart: add items, show summary, checkout
└── main()         # Runs the interactive menu loop
```

Key classes:

| Class | Responsibility |
|-------|----------------|
| `Colors` | Stores ANSI escape sequences used to color terminal text |
| `Coffee` | Simple data class holding a coffee's `name` and `price` |
| `Order` | Holds a list of `Coffee` items; supports adding, totaling, displaying, and checking out |

---

🛠️ Customization

Want to make it your own? A few easy tweaks:

- **Add a new coffee** — append a new `Coffee("Name", price)` entry to the `menu` list in `main()`, and remember to update the valid input range (`1 <= int(choice) <= 13` → adjust the upper bound) and the menu option numbers (`14`, `15`, `16`).
- **Change the color scheme** — edit the escape codes inside the `Colors` class.
- **Add discounts or taxes** — extend `Order.total()` or `Order.checkout()` with your own pricing logic.

---

🗺️ Roadmap Ideas

- [ ] Remove individual items from the cart
- [ ] Add coffee sizes (small/medium/large) with price modifiers
- [ ] Save order history to a file
- [ ] Add unit tests for `Order` and `Coffee`
- [ ] Package as an installable CLI (`pip install coffee-shop-cli`)

---

🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

📄 License

This project is available under the [MIT License](LICENSE).

---

<p align="center">Made with ☕ and Python</p>
