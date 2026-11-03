/// Buy-it-for-life math: cost per decade, replacement counts over a
/// horizon, and decade-cost comparisons between two items.
library;

/// One item priced on the decade scale.
class Item {
  final String name;
  final double price;

  /// Expected service life in years.
  final double years;

  const Item(this.name, this.price, this.years);
}

/// Price spread over ten years: [price] divided by [years] of use,
/// times ten. A $40 item that lasts 2 years costs $200 per decade.
double costPerDecade({required double price, required double years}) {
  final life = years < 0.5 ? 0.5 : years;
  return price / life * 10;
}

/// The item with the lower decade cost.
Item cheaperPerDecade(Item a, Item b) {
  final ca = costPerDecade(price: a.price, years: a.years);
  final cb = costPerDecade(price: b.price, years: b.years);
  return ca <= cb ? a : b;
}

/// How many times an item lasting [years] is rebought over [horizon] years.
int replacementCount({required double years, int horizon = 10}) {
  final life = years < 0.5 ? 0.5 : years;
  return (horizon / life).ceil();
}
