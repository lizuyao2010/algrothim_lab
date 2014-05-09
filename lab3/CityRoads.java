//cities.add("Duckburg");
//cities.add("Gotham City");
//cities.add("Metropolis");
//for (String city : cities) {
//	set.add(city);
//}
//setSize.add(1);
//setSize.add(1);
//setSize.add(1);
//cityDistanceList.add(new CityDistance("Duckburg", "Gotham City", 2324));
//cityDistanceList.add(new CityDistance("Duckburg", "Metropolis", 231));
//cityDistanceList.add(new CityDistance("Gotham City", "Metropolis", 2298));
//cityDistanceList = sortCityDistances();

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class CityRoads {
	private ArrayList<String> cities;
	private ArrayList<String> set;
	private ArrayList<Integer> setSize;
	private ArrayList<CityDistance> cityDistanceList;

	public CityRoads() {
		cities = new ArrayList<String>();
		set = new ArrayList<String>();
		setSize = new ArrayList<Integer>();
		cityDistanceList = new ArrayList<CityDistance>();
	}

	private ArrayList<CityDistance> sortCityDistances() {
		Object[] temp;
		temp = cityDistanceList.toArray();
		Arrays.sort(temp);
		ArrayList<CityDistance> sortedList = new ArrayList<CityDistance>();
		for (int i = 0; i < temp.length; i++) {
			sortedList.add((CityDistance) temp[i]);
		}
		return sortedList;
	}

	public void makeUnion(String city1, String city2) {
		int set1Index = cities.indexOf(city1);
		int set2Index = cities.indexOf(city2);
		if (setSize.get(set1Index) > setSize.get(set2Index)) {
			for (int i = 0; i < set.size(); i++) {
				if (set.get(i).compareTo(find(city2)) == 0) {
					int setIndex = set.indexOf(set.get(i));
					set.add(setIndex, find(city1));
					set.remove(setIndex + 1);
				}
			}
		} else {
			for (int i = 0; i < set.size(); i++) {
				if (set.get(i).compareTo(find(city1)) == 0) {
					int setIndex = set.indexOf(set.get(i));
					set.add(setIndex, find(city2));
					set.remove(setIndex + 1);
				}
			}
		}
	}

	public String find(String city) {
		int cityIndex = cities.indexOf(city);
		if (set.get(cityIndex).compareTo(city) != 0) {
			String newParent = find(set.get(cityIndex));
			set.remove(cityIndex);
			set.add(cityIndex, newParent);
			return newParent;
		}
		return city;
	}

	public int kruskal() {
		int totalWeight = 0;
		for (CityDistance cd : cityDistanceList) {
			String city1 = find(cd.city1);
			String city2 = find(cd.city2);
			if (city1.compareTo(city2) != 0) {
				makeUnion(city1, city2);
				totalWeight += cd.distance;
			}
		}
		return totalWeight;
	}

	public void parser() {
		Scanner scanner = new Scanner(System.in);
		while (scanner.hasNextLine()) {
			String line = scanner.nextLine().trim();
			if (!line.contains("--")) {
				if (line.startsWith("\"") && line.endsWith("\"")) {
					cities.add(line.substring(1, line.length() - 1));
					set.add(line.substring(1, line.length() - 1));
					setSize.add(1);
				} else {
					line.trim();
					cities.add(line);
					set.add(line);
					setSize.add(1);
				}
			} else {
				String[] splitLine = line.split("--");
				if (splitLine[0].startsWith("\"")
						&& splitLine[0].endsWith("\"")) {
					splitLine[0] = splitLine[0].substring(1,
							splitLine[0].length() - 1);
				}
				String[] secondSplitLine = splitLine[1].split("\\[");
				splitLine[1] = secondSplitLine[0].trim();
				secondSplitLine[1] = secondSplitLine[1].substring(0,
						secondSplitLine[1].length() - 1);
				if (splitLine[1].startsWith("\"")
						&& splitLine[1].endsWith("\"")) {
					splitLine[1] = splitLine[1].substring(1,
							splitLine[1].length() - 1);
				}
				cityDistanceList.add(new CityDistance(splitLine[0],
						splitLine[1], Integer.valueOf(secondSplitLine[1])));
			}
		}
		cityDistanceList = sortCityDistances();
	}

	private class CityDistance implements Comparable<CityDistance> {
		private String city1, city2;
		private int distance;

		public CityDistance(String city1, String city2, int distance) {
			this.city1 = city1;
			this.city2 = city2;
			this.distance = distance;
		}

		public int compareTo(CityDistance city2) {
			return distance - city2.distance;
		}
	}

	public static void main(String[] args) {
		CityRoads cr = new CityRoads();
		cr.parser();
		int weight = cr.kruskal();
		System.out.println(weight);
	}
}