import 'package:test/test.dart';
import 'package:cost_per_decade/cost_per_decade.dart';

void main() {
  test('decade cost', () {
    expect(costPerDecade(price: 150, years: 10), 150.0);
    expect(costPerDecade(price: 40, years: 2), 200.0);
  });

  test('comparison', () {
    const boots = Item('work boots', 150, 10);
    const cheap = Item('cheap boots', 40, 2);
    expect(cheaperPerDecade(boots, cheap).name, 'work boots');
  });

  test('replacement count', () {
    expect(replacementCount(years: 2), 5);
  });
}
