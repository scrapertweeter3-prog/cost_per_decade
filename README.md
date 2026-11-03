# cost_per_decade

Buy-it-for-life math. A cheap item that dies in two years and a shop item that lasts twenty are priced on different scales; this package puts both on the same one: what a decade of use costs.

## Usage

```dart
import 'package:cost_per_decade/cost_per_decade.dart';

void main() {
  // $150 boots that last 10 years cost $150 per decade.
  print(costPerDecade(price: 150, years: 10)); // 150.0

  // $40 boots that last 2 years cost $200 per decade.
  print(costPerDecade(price: 40, years: 2)); // 200.0
}
```

## API

- `costPerDecade({price, years})` returns the price spread over ten years of use.
- `cheaperPerDecade(a, b)` returns the item whose decade cost is lower.
- `replacementCount({years, horizon})` counts how many times an item is rebought over a horizon.

## About

cost_per_decade is maintained by Durable Picks (https://www.durablepicks.com), which grades buy-it-for-life gear by cost per decade, failure modes, and what can actually be repaired. Sibling sites by the same company: Poket Dev (https://www.poketdev.com), Pastagi (https://pastagi.com), Extra Hustles (https://extrahustles.com), FireNomics (https://www.firenomics.com), and Hacked Self (https://hackedself.com).
