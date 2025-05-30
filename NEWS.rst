v7.11.1
=======

No significant changes.


v7.11.0
=======

Features
--------

- Updated Malaysia calendar through 2027. (#35)


v7.10.0
=======

Features
--------

- Updated Ukraine holidays. (#32)
- Updated China for 2025. (#33)
- Removed Great Prayer Day from Denmark holidays from year 2024. (#34)


v7.9.1
======

Bugfixes
--------

- Remove observance shift for Italy (#29)
- Re-implement the logic of replace. (#31)


v7.9.0
======

Features
--------

- Coronation of His Majesty King Charles III Bank holiday in 2023 to the UK calendar.


v7.8.0
======

Features
--------

- Added China holidays for 2024.


v7.7.1
======

No significant changes.


v7.7.0
======

Features
--------

- Incorporate changes from workalendar v17.0.0 (2023-01-01)

  New calendars

  - New calendar: Added Tunisia calendar by @macharmi (#702)
  - New calendar: Added El Salvador calendar by @hersoncruz (#708).

  Other changes

  - Update China's public holidays for 2023 (#728).
  - Removed compatibility with Python 3.6, also, removed tests & amended documentation (#705).
  - Upgraded `tox` usage, now compatble with tox 4+ (added `allowlist_externals`).
  - Added support for Python 3.10 (#706).
  - Added support for Python 3.11 (#732).
  - Refactor ``NetherlandsWithSchoolHolidays.get_christmas_holidays`` for simplicity and readability.

- Incorporate changes from workalendar v16.4.0 (2022-09-16)

  - Fixed United Kingdom's 2022 holidays ; Added Bank Holiday for the State Funeral of Queen Elizabeth II (#719).

- Require Python 3.8 or later.


v7.6.1
======

Updated some latent references to peopledoc.

v7.6.0
======

Internal refactoring and simplification. Removed redundant "shift" holidays
from european countries.

v7.5.0
======

Incorporate changes from workalendar v16.3.0 (2022-02-22)

Calendars

- New calendar: Added Georgia (country) calendar by @atj01 (#687).
- New calendar: Added Kazakhstan calendar by @atj01 (#688).
- New calendar: Added USA Federal Reserve System calendar by @ludsoft (#695)

Bugfixes and other changes

- Removed duplicate Proclamation Day for Latvia, by @Daglina (#686).
- Documentation: Fix the ``keep_datetime`` usage example in the "basic" doc (#690).
- Added conditional holidays on 26th December and 2nd January in Neuchatel (Switzerland) (#697).
- Added Federal Thanksgiving Monday and two conditional holidays on 26th December and 2nd January in Neuchatel (Switzerland) (#697).

Incorporate changes from workalendar v16.2.0 (2021-12-10)

- Update China's public holidays for 2022, thx to @iamsk (#693).

Incorporate changes from workalendar v16.1.0 (2021-10-01)

- Fixed United Kingdom's 2022 holidays ; Spring Bank Holiday has been moved to the 3rd of June and Queen's Platinum Jubilee added to 2nd of June.
- New calendar: Added Guernsey calendar by @ludsoft (#681)

v7.4.0
======

Incorporate changes from workalendar v16.0.0 (2021-09-16)

Calendars

- New calendar: Added Philippines calendar by @micodls (#396)

Internal

- Remove `skyfield` dependency, added `[astronomy]` as extra dependency (#660).
- Replace `pyCalverter` with `convertdate` (#536).
- Remove unused `JalaliMixin`
- Replace `pkg_resources` with `importlib_metadata` to fetch the version number in `__init__.py` (#657)
- Added new badges (pypi, conda, license) and installation instructions (pip, conda) to readme file @sugatoray (#673).
- Added the "Workalendar maintainers" in the LICENSE file.
- Changed the maintainer email.

v7.3.0
======

Incorporate changes from workalendar v15.4.0 (2021-07-12)

- New calendar: Added Nigeria calendar by @taiyeoguns (#656)
- Fix: Chilean calendar floating dates, add Indigenous Peoples Day using solar term, thx @ajcobo.

Incorporate changes from workalendar v15.3.1 (2021-07-02)

Bugfixes

- Updated Japan calendar because of the Olympics, thx @lxlgarnett. (#662)
- Fixed Japan "Sports Day" label depending on the year.

Documentation

- The Workalendar project has been moved from Peopledoc's organization to its own (#651, #653, thx to @ewjoachim).

Incorporate changes from workalendar v15.3.0 (2021-05-07)

- Fix Barbados calendar to add 2 non computable public holiday and fix boxing day computation, thx to @ludsoft (#647).

Incorporate changes from workalendar v15.2.0 (2021-04-23)

- Fixed Cuiaba City calendar (Brazil), adding Easter Sunday, Corpus Christi and Good Friday, thx @leogregianin (#642).
- Fix Catalonian calendar: add missing St John the Baptist public holiday, thx @lozlow (#643).

Incorporate changes from workalendar v15.1.0 (2021-03-12)

- Bugfix: Bulgaria holidays are now computed using the Orthodox calendar, include shifting rules for holidays that fall on a week-end (#596).
- Bugfix: `get_working_days_delta` method to integrate the `extra_holidays` and `extra_working_days` args (#631).

Incorporate changes from workalendar v15.0.2 (2021-03-05)

- Bugfix: USA calendar would take the `shift_exceptions` into account, even if the exceptions are set in the next or previous year (#610).
- Requirements: Unpin `pyupgrade` library (#634).

Incorporate changes from workalendar v15.0.1 (2021-02-26)

- Hotfix: Taiwan exceptional working day on February, 20th 2021 (#628).
- Hotfix: September 11th is a working day in Taiwan (#628).

v7.2.0
======

Incorporate changes from workalendar v15.0.0 (2021-02-19)

Major changes

- API: New method available in `core` module: `Calendar.get_iso_week_date()` to find the weekday X of the week number Y (#619).
- Requirements: Replace pytz with `(backports.)zoneinfo`, thx to @eumiro (#614)
- Doc: Documented the different (in)compatibilities due to the use of `zoneinfo` (#614).

Bugfixes

- Small fixes in Netherlands School calendars (#619).
- Temporary downgrade of `pyupgrade` to fix the `pyup_dirs`.

Improving test coverage

- Improve Netherlands coverage (#546, #619).
- Improve Russia coverage (#546).
- Improve USA calendar coverage by removing a method that wasn't used anyways (`get_washington_birthday_december()`). The method is implemented in both Indiana and Georgia State calendars, and is specific for each state, even if they look very similar (#546).
- Improve the `astronomy.py` module coverage (#546).
- Improve coverage for the `tests/__init__.py` module (#546). *Note:* system-dependant test branch (if Windows) won't be counted for coverage.

v7.1.0
======

Incorporate changes from workalendar v14.3.0 (2021-01-15)

Calendars

- Update Malaysia 2022-2024 (Deepavali + Thaipusam) by @jack-pace

Incorporate changes from workalendar v14.2.0 (2021-01-08)

Calendars

- Update Singapore for range from 2022 to 2030 (Deepavali), by @hprobotic

Internal

- Replace `os.path.*` calls with `pathlib.Path`, thx to @eumiro (#603)
- Use f-string for string formatting, thx to @eumiro (#605)
- Simplify collections handling, thx to @eumiro (#606)
- Use integers for time units divisions, thx to @eumiro
- Adding Mac OS & Windows tests to the test matrix (related to #607).
- Fix tests when running them on Windows (#607).

v7.0.0
======

New feature

- Enhanced support for multi-day "series" holidays such as Chinese Spring
  Festival and Islamic Eid. Previously, if one day of the series was shifted
  as per the observance shift rules, it would "merge" into the next day of the
  series, effectively shortening the observed series. Now, all the following
  days of the series are shifted, maintaining its duration.

Incorporate changes from workalendar v14.1.0 (2020-12-10)

- Fix Russia 2021 holidays, thx @MichalChromcak for the bug report (#578).

Incorporate changes from workalendar v14.0.0 (2020-11-27)

- Fixes

  - Fix Russia calendar: non-working days are shifted to the next MON when they happen on the week-end (#589).
  - Fix Russia New year holidays. It has become a week off since 2005 (related to #578).
  - Added Russia COVID-19 non-working days for the year 2020 ; these days are not shifted to next MON (#578).
  - Fixed Russia Christmas day ; December 25th is not a public holiday. Fixed several other Orthodox calendars (#530).
  - Update China's public holidays for 2021, thanks @iamsk.

- Minor changes

  - Added a `daterange` function in `workalendar.core` module to iterate between two dates.

Incorporate changes from workalendar v13.0.0 (2020-11-13)

- Calendars

  - Add optional school holidays to Netherlands calendar, by @Flix6x (#556).
  - Add optional carnival to Netherlands calendar.

- Documentation

  - Moving the `contributing.md` file to the `docs/` directory (#573).
  - Changed from `setup.py` to a nice `setup.cfg` file, thanks @ewjoachim (#576).
  - Added documentation about class options (#572).
  - Converted `README.rst` file into `README.md` (#575).
  - Fixed Pull Request template to reference `setup.cfg` (#587).

- Other changes

  - Switched from Travis CI to Github Actions for CI jobs, thanks to @mgu.
  - Added support of Python 3.9 (#557).
  - Changed from `setup.py` to a nice `setup.cfg` file, thanks @ewjoachim (#576).
  - Use the `setup.cfg` file in the key to cache in `ci.yml` file (#587).
  - [OBSOLETE] Switched from bionic to focal on Travis CI (we've switched to GH actions after that).

Incorporate changes from workalendar v12.1.0 (2020-10-16)

- New calendars

  - Added Spain regions: Andalusia, Aragon, Castile and León, Castilla-La Mancha, Canary Islands, Extremadura, Galicia, Balearic Islands, La Rioja, Community of Madrid, Murcia, Navarre, Asturias, Basque Country, Cantabria, Valencian Community (#531).
  - Added all ISO codes for Spain regions - thx @ainarela for your help on this (#531).

- Other changes

  - Refactored Spain test modules (#531).
  - Fix Catalonia calendar by removing *Sant Juan* day, which does not appear to be an official holiday (#531).
  - Improve coverage of `workalendar/core.py` module (#546).
  - Improve coverage for the Netherlands calendar - Queen's Day (#546).
  - Improve coverage for the Romania calendar - Liberation day (#546).
  - Improve coverage for the New Zealand calendar (#546).
  - Added a tox entrypoint to ensure code is Python 3.6+, using ``pyupgrade`` (#566).
  - Added the pyupgrade tox job to the test suite, amended contributing documentation (#566).

Incorporate changes from workalendar v12.0.0 (2020-10-02)

- **Deprecation:** Dropped support for Python 3.5. As of this version, workalendar now requires Python 3.6+ (#330).
- Improve coverage of Singapore calendar (#546).

Incorporate changes from workalendar v11.0.1 (2020-09-11)

- Add ISO code decorator to Catalonia calendar, thanks to @jbagot (#551).
- Improve coverage of South Africa calendar (#546).
- Improve coverage of Brazil calendar (#546).
- Improve coverage of Canada (Nunavut) calendar (#546).
- Improve coverage of Israel calendar (#546).

Incorporate changes from workalendar v11.0.0 (2020-09-04)

- New calendar

  - Added Mozambique calendar by @mr-shovel (#542).

- New feature

  - Added iCal export feature, initiated by @joooeey (#197).
  - Fix PRODID pattern for iCal exports: `"PRODID:-//workalendar//ical {__version__}//EN"`, using current workalendar version (#543).

Incorporate changes from workalendar v10.4.0 (2020-08-28)

- New calendar

  - Added Monaco calendar by @joaopbnogueira (#538).

- Major changes and bugfixes

  - Migrating Labour Day as a worldwide holiday, disabled by default, but activated (to date) for about 50 countries (including label change when necessary), `contributing.md` documentation amended (#467).
  - Bugfix: Avoid Cesar Chavez Day duplicated shifts by refactoring the California shift rules (#528).

- Other changes

  - Small refactoring for the Colombia / added docstrings & comments to explain why we're not using stock options. Added tests for year 2020 and handling shift exceptions (#509).
  - Tech: Replace occurrences of `assertEquals` with `assertEqual` to clear warnings (#533).
  - Use `include_immaculate_conception` flag for Portugal, Brazil, Argentina, Paraguay calendars (#529).

Incorporate changes from workalendar v10.3.0 (2020-07-10)

- Bugfixes

  - Belarus: removing day after Radonitsa, which is apparently not a holiday.
  - Algeria: assigning the week-end days as FRI+SAT, as it's following a Islamic calendar.

- Other changes

  - Refactoring the core ``Calendar`` classes / mixins for better understanding. Only one ``Calendar`` subclass should be imported / used in calendar classes, the rest (when possible) should be ``Mixins`` (related to #511).
  - Declaring the New year's Day as a worldwide holiday, with only two exceptions (to date): Israel & Qatar (#511).
  - Fixed `contributing.md` documentation with the new class/mixin organization (#511).

Incorporate changes from workalendar v10.2.0 (2020-06-26)

- Bugfix: setting *Consciência Negra day* as a non-holiday by default for Brazilian calendars, thx to @edniemeyer (#516).
- Bugfix: Introducing the changes in Croatia holidays as of 2020 - Remembrance Day, Independence Day, Statehood Day... thx to @davidpodrebarac for the bug report (#515).

Incorporate changes from workalendar v10.1.0 (2020-06-18)

- Calendar fix

  - Adding All Souls' Day to Lithuania calendar, starting of 2020, thx to @norkunas (#512).

- Minor changes

  - Small fixes (docstrings, use of extends, etc) on Cayman Islands calendar (#507).
  - Moving Carnaval / Mardi Gras / Fat Tuesday calculation into the `workalendar.core` module, because it's used in at least 3 countries and some States / Counties in the USA.

Incorporate changes from workalendar v10.0.0 (2020-06-05)

- **BREAKING CHANGE**: the ``IsoRegistry.get_calendar_class()`` method has been removed from the code and should no longer be used (#375, #495).

Incorporate changes from workalendar v9.2.0 (2020-06-02)

- New Calendars

- Added rules for all Switzerland Cantons, branching off the initial work by @brutasse (#497).

Incorporate changes from workalendar v9.0.1 (2020-05-22)

- Making the Israel calendar more efficient (#498).
- Fixing duplicated holidays in Hong-Kong and Hong-Kong Bank holiday calendars (#496).
- Integrating Hong-Kong holidays for 2021 (#496).

Incorporate changes from workalendar v9.0.0 (2020-04-24)

- **BREAKING CHANGE**: the ``IsoRegistry.items()`` method has been removed from the API. You must use the ``get_calendars()`` to perform the same registry queries (#375, #491).
- *Deprecation notice*: The usage of ``IsoRegistry.get_calendar_class()`` is strongly discouraged, in favor of ``get()``. The ``get_calendar_class`` method will be dropped in a further release. In the meantime, they'll be both equivalent (#375, #418).

Incorporate changes from workalendar v8.4.0 (2020-04-17)

- New Calendar

  - Added Kenyan calendar, by @KidkArolis (#484)

- Minor fixes

  - Fixed Lithuania calendar to use the core flags for Assumption and All Saints (#468).
  - Fixed Malta calendar ; January 1st was already included, no need to add it to the ``FIXED_HOLIDAYS`` property (#469).
  - Small refactor in Netherlands calendar to use core constants (#470).

Incorporate changes from workalendar v8.3.0 (2020-04-14)

- Fixing Hong-Kong calendar, where SAT are common working days (#477).
- Introducing Hong-Kong Bank calendar. For banks, Saturdays are non-working days (#477).

Incorporate changes from workalendar v8.2.2 (2020-04-10)

- Fixed Argentina's "Malvinas Day" date for 2020, shifted to March 31st because of the coronavirus crisis (#476).
- Fixed Argentina's label for "Malvinas Day" and "Día de la Memoria" (#476).

Incorporate changes from workalendar v8.2.1 (2020-04-03)

- Added BrazilBankCalendar to support `include_` flags and make it possible to extend and change these flags to support custom bank calendars (#474).

Incorporate changes from workalendar v8.2.0 (2020-03-13)

- Added Belarus calendar, by @alexdoesstuff (#472).

Incorporate changes from workalendar v8.1.0 (2020-02-07)

- Added Israel holidays eves and removed holidays which are not affecting the working days in Israel (#461).
- Fix warning in China's holidays to dynamically read supported years, thx @fredrike (#459).

Incorporate changes from workalendar v8.0.2 (2020-01-24)

- Fix several miscalculations in Georgia (USA) calendar (#451).

Incorporate changes from workalendar v8.0.1 (2020-01-24)

- Fix Family Day for British Columbia (Canada) which was switched from 2nd to 3rd Monday of February in 2019 - thx @jbroudou for the bug report (#454).

v6.1.2
======

#14: Replaced implicit dependency on setuptools with explicit
dependency on importlib.metadata.

v6.1.1
======

Fix version inference when installed from sdist.

v6.1.0
======

Incorporate changes from workalendar v8.0.0 (2020-01-10)

- **BREAKING CHANGE** Drop Support for Python 2 - EOL January 1st 2020 (#442).
- Added Ukraine calendar, by @apelloni.
- Small cleanup in the ``.travis.yml`` file, thx to @Natim.

- Changes in the ``registry.items()`` method API.
  - This method is aliased to ``get_calendars()``. In a near release, the ``items()`` method will change its purpose.
  - The ``get_calendars()`` method accepts an empty/missing ``region_codes`` argument to retrieve the full registry. Please see the [ISO Registry documentation](https://workalendar.github.io/workalendar/iso-registry.html) for extensive usage docs (#403, #375).

Incorporate changes from workalendar v7.2.0 (2019-12-06)

New calendars

- Added Serbia calendar, by @apelloni (#435).
- Added Argentina calendar, by @ftatarli (#419).

Other changes

- Update China's public holidays for 2020, thx @nut-free (#429).
- Update Malaysia and Singapore for 2021 (Deepavali + Thaipusam) by @jack-pace (#432).
- Small refactorings on the Gevena (Switzerland) holiday class, thx to @cw-intellineers (#420).

Incorporate changes from workalendar v7.1.1 (2019-11-22)

- **Bugfix** for USA: Fixed incorrect implementation for Thanksgiving Friday, thx @deveshvar (#422).
- Fix Advanced usage documentation about Thanksgiving Day (#426).
- Added Geneva calendar by @cw-intellineers (#420).

Incorporate changes from workalendar v7.1.0 (2019-11-15)

New calendars

- Added 27 Brazil calendars -- thanks a lot to @luismalta & @mileo, (#409 & #415)

Enhancements

- Added compatibility with Python 3.8 (#406).
- Added an IBGE_REGISTER to reference IBGE (brazilian) calendars with related tests (#415).
- Improve ISO registry interface by raising an error when trying to register a non-Calendar class (#412).

Other changes

- Fixes and additions to some Brazil calendars ; again, thanks to @luismalta & @mileo, (#409 & #415)
- Fix Denmark, re-add Christmas Eve, which is widely treated as public holiday ; thx to @KidkArolis, (#414).
- Increase Malaysia coverage by adding tests for missing Deepavali & Thaipusam.
- Increase China coverage by adding tests for special extra-holidays & extra-working days cases.

v6.0.0
======

Require Python 3.6 or later.

v5.0.0
======

#11: Add support for ``__add__`` and ``__sub__`` for
``Holiday`` instances on Python 3.8 and later. Now adding
a timedelta to a ``Holiday`` returns another ``Holiday``.

Incorporate changes from workalendar v7.0.0 (2019-09-20)

- Drop `ephem` astronomical calculation library, in favor of `skyfield` and `skyfield-data` for providing minimal data files to enable computation (#302, #348). Many thanks to @GammaSagittarii for the tremendous help on finding the right way to compute Chinese Solar Terms. Also thanks to @antvig and @DainDwarf for testing the beta version (#398).

Incorporate changes from workalendar v6.0.1 (2019-09-17)

- Fix Turkey Republic Day (#399, thx to @mhmtozc & @Natim).

Incorporate changes from workalendar v6.0.0 (2019-08-02)

- **Deprecation Notice:** *The global ISO registry now returns plain `dict` objects from its various methods.*
- Global registry now returns plain built-in dicts (#375).
- Removed `EphemMixin` in favor of astronomical functions (#302).
- Added first day counting when computing working_days delta (#393), thx @Querdos.

Incorporate changes from workalendar v5.2.3 (2019-07-11)
- Fix Romania, make sure Easter and related holidays are calculated using the Orthodox calendar, thx to @KidkArolis (#389).


v4.0.0
======

Incorporate changes from workalendar v5.2.2. (2019-07-07)

- **Deprecation Warning:** *Currently the registry returns `OrderedDict` objects when you're querying for regions or subregions. Expect that the next major release will preferrably return plain'ol' `dict` objects. If your scripts rely on the order of the objects returned, you'll have to sort them yourself.*
- Fix Denmark, remove observances (remove Palm Sunday, Constitution Day, Christmas Eve and New Year's Eve) (#387, #386)

Incorporate changes from workalendar v5.2.1 (2019-07-05)

- Refactored the package building procedure, now linked to `make package` ; added a note about this target in the PR template (#366).
- Fixed United Kingom's 2020 holidays ; The Early May Bank Holiday has been moved to May 8th to commemorate the 75th anniversary of the end of WWII (#381).

Incorporate changes from workalendar v5.2.0 (2019-07-04)

- New Calendar

    - Added JapanBank by @raybuhr (#379, #369).

- Other changes

    - Added adjustments to 2019-2020 Japan calendar due to the coronation of a new emperor (#379).
    - Add a note about the fact that contributors should not change the version number in the changelog and/or the ``setup.py`` file (#380).

Incorporate changes from workalendar v5.1.1 (2019-06-27)

- Display missing lines in coverage report (#376).
- Add "Europe Day" for Luxembourg (#377).

Incorporate changes from workalendar v5.1.0 (2019-06-24)

- New Calendar

    - Added Turkey by @tayyipgoren (#371).

- Other changes

    - Change registry mechanism to avoid circular imports (#288).
    - Internal: Added a "Release" section to the Pull Request template.
    - Internal: Added advices on the Changelog entry in the Contributing document.
    - Bugfix: Fixing North Carolina shift rules when Christmas Day happens on Saturday (#232).
    - Documentation: rearrange country list in ``README.rst`` (sorting and fixing nested lists).
    - Documentation: Renamed and changed format of the "Contributing guidelines" document, now in Markdown (GFM variant), with a few fixes (#368).
    - Internal: remove coverage targets ; now coverage reports are displayed for each tox job, but they won't output classes with 100% coverage.

Incorporate changes from workalendar v5.0.3 (2019-06-07)

- Bugfix: Panama - Fixed incorrect independence from Spain date, thanks to @chopanpma (#361).

Incorporate changes from workalendar v5.0.2 (2019-06-03)

- Bugfix: Israel - Fixed incorrect Purim/Shushan Purim dates in jewish leap years, thx @orzarchi. This fix cancels the last (5.0.1) version, that will be deleted from PyPI.

Incorporate changes from workalendar v5.0.1 (2019-06-03)

- **WARNING** This version contains known bugs on Israel calendar. Please do not use it in production.

- Bugfix: Israel - Fixed incorrect Purim/Shushan Purim dates in jewish leap years, thx @orzarchi.

Incorporate changes from workalendar v5.0.0 (2019-05-24)

- Major Changes & fixes

    - Dropped Python 3.4 support (#352).
    - Added Malaysia Thaipusam days for the year 2019 & 2020 - thx @burlak for the bug report (#354).
    - Fixed Deepavali dates for the year 2018 ; confirmed fixed dates that were set in the past.

- Added calendars

    - Added Florida specific calendars: Florida Legal, Florida Circuit Courts, Miami-Dade (#216).

Incorporate changes from workalendar v4.4.0 (2019-05-17)

- **WARNING**: This release will be the last one to support Python 3.4, which has [reached its End of Life and has been retired](https://www.python.org/dev/peps/pep-0429/#release-schedule). Please upgrade.

- Added calendar

    - Added California specific calendars: California Education, Berkeley, San Francisco, West Hollywood (#215).

- Fixes

    - Added a few refactors and tests for Australia Capital Territory holiday named "Family & Community Day", that lasted from 2007 to 2017 (#25).
    - Added South African 2019 National Elections as holiday (#350), by @RichardOB.

Incorporate changes from workalendar v4.3.1 (2019-05-03)

- Bugfix: Update 2019 Labour Day Holidays for China as changed by government recently (2019-03-22), by @iamsk, and thanks to @ltyely for their patch (#345 & #347).

Incorporate changes from workalendar v4.3.0 (2019-03-15)

- New Calendar

    - Added Barbados by @ludsoft.

- Fixes

    - Added isolated tests for shifting mechanics in USA calendars - previously untested (#335).
    - Added Berlin specific holidays (#340).
    - Added several one-off public holidays to UK calendar (#336).

Incorporate changes from workalendar v4.2.0 (2019-02-21)

- New calendars

    - Added several US territories and other specific calendars:

        - American Samoa territory (#218).
        - Chicago, Illinois (#220).
        - Guam territory (#219).
        - Suffolk County, Massachusetts (#222).

    - Added Cayman Islands, British Overseas Territory (#328)

Incorporate changes from workalendar v4.1.0 (2019-02-07)

- New calendars

- **WARNING** Scotland (sub)calendars are highly experimental and because of their very puzzling rules, may be false. Please use them with care.

    - Added Scotland calendars, i.e. Scotland, Aberdeen, Angus, Arbroath, Ayr, Carnoustie & Monifieth, Clydebank, Dumfries & Galloway, Dundee, East Dunbartonshire, Edinburgh, Elgin, Falkirk, Fife, Galashiels, Glasgow, Hawick, Inverclyde, Inverness, Kilmarnock, Lochaber, Monifieth, North Lanarkshire, Paisley, Perth, Scottish Borders, South Lanarkshire, Stirling, and West Dunbartonshire (#31).

- Bugfixes

    - Fixed United Kingdom bank holiday for 2002 and 2012, thx @ludsoft (#315).
    - Fix a small flake8 issue with wrong indentation (#319).
    - Fix Russia "Day of Unity" date, set to November 4th, thx @alexitkes for the bug report (#317).

Incorporate changes from workalendar v4.0.0 (2019-01-24)

- Solved the incompatibility between `pandas` latest version and Python 3.4. Upgraded travis distro to Xenial/16.04 LTS (#307).
- Added instructions about the usage of the `iso_register` decorator in the pull-request template (#309).

- New Calendars

    - Added New Zealand, by @johnguant (#306).
    - Added Paraguay calendar, following the work of @reichert (#268).
    - Added China calendar, by @iamsk (#304).
    - Added Israel, by @armona, @tsehori (#281).

3.0
===

Incorporate changes from workalendar 3.2.1:

- Added DEEPAVALI days for 2019 and 2020, thx @pvalenti (#282).
- Fixed Germany Reformation Day miscalculation. Some German states include Reformation Day since the "beginning" ; in 2017, all states included Reformation Day as a holiday (500th anniversary of the Reformation) ; starting of 2018, 4 states added Reformation Day (#295).

Incorporate changes from workalendar 3.2.0:

- Removed dependency to `PyEphem`. This package was the "Python2-compatible" library to deal with the xephem system library. Now it's obsolete, so you don't need this dual-dependency handling, because `ephem` is compatible with Python 2 & Python 3 (#296).
- Raise an exception when trying to use unsupported date/datetime types. Workalendar now only supports stdlib `date` & `datetime` (sub)types. See the `basic documentation <https://workalendar.github.io/workalendar/basic.html#standard-datetime-types-only-please>`_ for more details (#294).

Incorporate changes from workalendar 3.1.1:

- Fixed ISO 3166-1 code for the `Slovenia` calendar (#291, thx @john-sandall).

Incorporate changes from workalendar 3.1.0:

- Added support for Python 3.7 (#283).
- Fixed the `SouthAfrica` holidays calendar, taking into account the specs of holidays that vary over the periods. As a consequence, it cleaned up erroneous holidays that were duplicated in some years (#285). Thx to @surfer190 for his review & suggestions.
- Bugfix for South Africa: disabled the possibility to compute holidays prior to the year 1910.
- Renamed Madagascar test class name into `MadagascarTest` (#286).
- Separated the coverage jobs from the pure tests. Their report output was disturbing in development mode, you had to scroll your way up to find eventual failing tests (#289).

Incorporate changes from workalendar 3.0.0:

Large work on global registry: refs (#13), (#96), (#257) & (#284).

- Added Tests for Europe registry.
- Revamped and cleaned up Europe countries.
- Added the United States of America + States, American countries & sub-regions, African countries, Asian countries, Oceanian countries.
- The global registry usage is documented.
- Changed Canada namespace to `workalendar.america.canada`.
- You don't have to declare a `name` properties for Calendar classes. It will be deducted from the docstring.
- Changed the `registry.items()` mandatory argument name to `region_codes` for more readability.

Incorporate changes from workalendar 2.6.0:

- Added Angola, by @dvdmgl (#276)
- Portugal - removed carnival from Portuguese holidays, restored missing holidays (#275)
- Added All Souls Day to common (#274)
- Allow the `add_working_days()` function to be provided a datetime, and returning a `date` (#270).
- Added a `keep_datetime` option to keep the original type of the input argument for both ``add_working_days()`` and ``sub_working_days()`` functions (#270).
- Fixed usage examples of ``get_first_weekday_after()`` docstring + in code (calendars and tests) ; do not use magic values, use MON, TUE, etc (#271).
- Turned Changelog into a Markdown file (#272).
- Added basic usage documentation, hosted by Github pages.
- Added advanced usage documentation.

Incorporate changes from workalendar 2.5.0:

- Bugfix: deduplicate South Africa holidays that were emitted as duplicates (#265).
- Add the `get_working_days_delta` method to the core calendar class (#260).

Incorporate changes from workalendar 2.4.0:

- Added Lithuania, by @landler (#254).
- Added Russia, by @vanadium23 (#259).
- Fixed shifting ANZAC day for Australia states (#249).
- Renamed Australian state classes to actual state names(eg. AustraliaNewSouthWales to NewSouthWales).
- Update ACT holidays (#251).
- Fixing Federal Christmas Shift ; added a `include_veterans_day` flag to enable/disable Veteran's day on specific calendar - e.g. Mozilla's dedicated calendar (#242).
- **Deprecation:** Dropped support for Python 3.3 (#245).
- Fixed Travis-ci configuration for Python 3.5 and al (#252).
- First step iteration on the "global registry" feature. European countries are now part of a registry loaded in the ``workalendar.registry`` module. Please use with care at the moment (#248).
- Refactored Australia family and community day calculation (#244).

2.0
===

Incorporate changes from workalendar 2.1.0:

- Added Hong Kong, by @nedlowe (#235).
- Splitted `africa.py` file into an `africa/` module (#236).
- Added Alabama Counties - Baldwin County, Mobile County, Perry County. Refactored UnitedStates classes to have a parameter to include the "Mardi Gras" day (#214).
- Added brazilian calendar to consider working days for bank transactions, by @fvlima (#238).

Incorporate changes from workalendar 2.0.0:

- Major refactor in the USA module. Each State is now an independant module, all of the Mixins were removed, all the possible corrections have been made, following the main Wikipedia page, and cross-checking with official sources when it was possible (#171).
- Added District of Columbia in the USA module (#217).
- Run tests with Python3.6 in CI (#210)
- Small refactors / cleanups in the following calendars: Hungary, Iceland, Ireland, Latvia, Netherlands, Spain, Japan, Taiwan, Australia, Canada, USA (#209).
- Various refactors for the Asia module, essentially centered around a more convenient Chinese New Year computation toolset (#202).
- Refactoring the USA tests: using inheritance to test federal and state-based holidays using only one "Don't Repeat Yourself" codebase (#213).

Incorporate changes from workalendar 1.3.0:

- Added Singapore calendar, initiated by @nedlowe (#194 + #195).
- Added Malaysia, by @gregyhj (#201).
- Added Good Friday in the list of Hungarian holidays, as of the year 2017 (#203), thx to @mariusz-korzekwa for the bug report.
- Assigned a minimal setuptools version, to avoid naughty ``DistributionNotFound`` exceptions with obsolete versions (#74).
- Fixed a bug in Slovakia calendar, de-duplicated Christmas Day, that appeared twice (#205).
- Fixed important bugs in the calendars of the following Brazilian cities: Vitória, Vila Velha, Cariacica, Guarapari and Serra - thx to Fernanda Gonçalves Rodrigues, who confirmed this issue raised by @Skippern (#199).

Incorporate changes from workalendar 1.2.0:

- Moved all the calendar of countries on the american continent in their own modules (#188).
- Refactor base Calendar class get_weekend_days to use WEEKEND_DAYS more intelligently (#191 + #192).
- Many additions to the Brazil and various states / cities. Were added: Acre, Alagoas, Amapá, Amazonas, Bahia, Ceará, Distrito Federal, Espírito Santo State, Goiás, Maranhão, Mato Grosso, Mato Grosso do Sul, Pará, Paraíba, Pernambuco, Piauí, Rio de Janeiro, Rio Grande do Norte, Rio Grande do Sul, Rondônia, Roraima, Santa Catarina, São Paulo, Sergipe, Tocantins, City of Vitória, City of Vila Velha, City of Cariacica, City of Guarapari and City of Serra (#187).
- Added a ``good_friday_label`` class variable to ``ChristianMixin`` ; one can assign the right label to this holiday (#187).
- Added a ``ash_wednesday_label`` class variable to ``ChristianMixin`` ; one can assign the right label to this holiday (#187).

Incorporate changes from workalendar 1.1.0:

- Added Cyprus. thx @gregn610 (#174).
- Added Latvia. thx @gregn610 (#178).
- Added Malta. thx @gregn610 (#179).
- Added Romania. thx @gregn610 (#180).
- Added Canton of Vaud (Switzerland) - @brutasse (#182).
- Fixed January 2nd state holiday (#181).
- Fixed Saxony repentance day for the year 2016. thx @Natim (#168).
- Fixed Historical and one-off holidays for South Africa. thx @gregn610 (#173).
- Minor PEP8 fixes (#186).

Incorporate changes from workalendar 1.0.0:

- Add Ireland. thx @gregn610 (#152).
- Bugfix: New Year's Eve is not a holiday in Netherlands (#154).
- Add Austria.  thx @gregn610 (#153)
- Add Bulgaria. thx @gregn610 (#156)
- Add Croatia. thx @gregn610 (#157)

Incorporate changes from workalendar 0.8.1:

- Reformation Day is a national holiday in Germany, but only in 2017 (#150).

1.8
===

Now tests are run using tox and releases are made automatically
using Travis-CI deployment framework.

Incorporate changes from workalendar 0.8.0:

- Fix Czech Republic calendar - as of 2016, Good Friday has become a holiday (#148).

Incorporate changes from workalendar 0.7.0:

- Easter Sunday is a Brandenburg federate state holiday (#143), thx @uvchik.
- Added Catalonia (#145), thx @ferranp.
- Use `find_packages()` to fetch package directories in `setup.py` (#141, #144).
- use py.test instead of nosetests for tests (#146).
- cleanup: remove unused ``swiss.py`` file (#147).

Incorporate changes from workalendar 0.6.1:

- Added Estonia, thx to @landler (#134),
- Europe-related modules being reorganized, thx to @Natim (#135),
- Fixed King / Queen's day in Netherlands, thx to @PeterJacob (#138),
- Added a pull-request template (#125),
- Added a Makefile for various dev-related tasks -- installs, running tests, uploading to PyPI... (#133).

1.7.1
=====

- #7: Avoid crashing on import when installed as zip package.

1.7
===

Incorporate changes from workalendar 0.5.0:

- A new holiday has appeared in Japan as of 2016 (#131), thx @suhara for the report.

Incorporate changes from workalendar 0.4.5:

- Added Slovenia, thx to @ratek1 (#124).
- Added Switzerland, thx to @sykaeh (#127).

1.6
===

- #6: Remove observance shift for Sweden.
- Use `jaraco skeleton <https://github.com/jaraco/skeleton>`_ to
  maintain the project structure, adding automatic releases
  from continuous integration and bundled documentation.

1.5
===

Incorporate changes from workalendar 0.4.3:

- Added Denmark (#117).
- Tiny fixes in the ``usa.py`` module (flake8 + typo) (#122)
- Added datetime to date conversion in is_holiday() (#118)
- Added function to get the holiday label by date (#120)
- Moved from `novapost` to the `novafloss` organization, handling FLOSS projects in People Doc Inc. (#116)
- Added Spain 2016 (#123)

Incorporate changes from workalendar 0.4.2:

- Added Luxembourg (#111)
- Added Netherlands (#113)
- Added Spain (#114)
- Bugfix: fixed the name of the Pentecost for Sweden (#115)

Incorporate changes from workalendar 0.4.1:

- Added Portugal, thx to @borfast (#110).

Incorporate changes from workalendar 0.4.0:

- Added Colombia calendar, thx to @spalac24
- Added Slovakia calendar, thx to @Adman
- Fixed the Boxing day & boxing day shift for Australia

1.4
===

``Calendar.get_observed_date`` now allows ``observance_shift`` to be
a callable accepting the holiday and calendar and returning the observed
date. ``Holiday`` supplies a ``get_nearest_weekday`` method suitable for
locating the nearest weekday.

- #5: USA Independence Day now honors the nearest weekday model.

1.3
===

Incorporate these fixes from Workalendar 0.3:

- ``delta`` argument for ``add_working_days()`` can be negative. added a
  ``sub_working_days()`` method that computes working days backwards.
- BUGFIX: Renaming Showa Day. "ō is not romji" (#100) (thx @shinriyo)
- BUGFIX: Belgian National Day title (#99) (thx @laulaz)

1.2.1
=====

Correct usage in example.

1.2
===

Fixed issue #4 where Finland holidays were shifted but shouldn't have been.
Calendars and Holidays may now specify observance_shift=None to signal no
shift.

Package can now be tested with pytest-runner by invoking ``python setup.py
pytest``.

1.1.3
=====

Fix name of Finnish Independence Day.

1.1.2
=====

Fixed issues with packaging (disabled installation an zip egg and now use
setuptools always).

1.1
===

UnitedKingdom Calendar now uses indicated/observed Holidays.

Includes these changes slated for workalendar 0.3:

- BUGFIX: shifting UK boxing day if Christmas day falls on a Friday (shift to
  next Monday) (#95)

1.0
===

Initial release of Calendra based on Workalendar 0.2.

- Adds Holiday class per (#79). Adds support for giving
  holidays a more rich description and better resolution of observed versus
  indicated holidays. See the pull request for detail on the motivation and
  implementation. See the usa.UnitedStates calendar for example usage.

Includes these changes slated for workalendar 0.3:

- Germany calendar added, thx to @rndusr
- Support building on systems where LANG=C (Ubuntu) (#92)
- little improvement to directly return a tested value.
