# Firefox Auto Search

This Python script makes use of Firefox's smart keyword feature.

By right-clicking on a search field on a webpage and choosing "Add a Keyword...", a user can associate a smart keyword with this search field.

This script allows mass-searching a list of queries using this Firefox feature. Smart Keywords are documented [here (Mozilla's website)](https://support.mozilla.org/en-US/kb/how-search-from-address-bar).

## Example

Suppose a user has registered the YouTube.com search field as a smart keyword, named "yt". This allows them to type "yt cats" to search for cat videos on YouTube.

`keyword.txt` contains "yt" and `queries.txt` contains "cats" and "dogs". Running the script opens YouTube search tabs for "cats" and "dogs".

This script is especially useful for people who wish to monitor various ads. One could use it on e-commerce websites like eBay or Amazon. It could help to monitor housing in multiple locations.

## Features

- **Keyword and Query Files**: Specify the keyword and queries in separate text files for easy customization.
- **Efficient Automation**: Utilizes Selenium WebDriver to interact with Firefox.

## Prerequisites

- Windows (tested on Windows 10).
- Python
- Install required packages: `pip install selenium keyboard`

## Usage

1. **Add Smart Keyword to Firefox**: If you haven't done it yet, [add the smart keyword you'll be using to Firefox](https://support.mozilla.org/en-US/kb/how-search-from-address-bar).
2. **Prepare Files**: Fill in 'type_keyword_here.txt' and 'type_queries_here.txt'.
3. **Run Script**: Execute `firefox_auto_search.py`.
4. **Sit Back and Relax**: Firefox opens tabs with search results. **Do not click with your mouse/use your keyboard while the script is running**

## Limitations/Issues

- Not every search field can be associated with smart keywords. It doesn't work on Reddit, for instance.
- The script requires Firefox to be closed before launch.
- It can have issues with focusing Firefox. Again, do not click with your mouse/use your keyboard while the script is running. If the script fails, either try to click on Firefox as soon as it launches so it gets focused, or raise the `time_sleep()` input value.
- Haven't tested it on another setup. It might run too fast for low-end PCs. If so, you might want to raise the `time_sleep()` input value.
- I have yet to clean up the code and comment it.

## Contributions

Contributions welcome! Open issues or pull requests for suggestions, bug reports, or feature requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

