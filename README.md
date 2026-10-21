# Ulauncher Pinyin Tones

![Pinyin Tones icon](images/icon.png)

A [Ulauncher](https://ulauncher.io) extension that converts pinyin with tone numbers into pinyin with tone marks.

```text
pyt ni3 hao3    →  nǐ hǎo
pyt Zhong1guo2  →  Zhōngguó
pyt lv4         →  lǜ
```

Press `Enter` to copy the result to the clipboard.

## Requirements

Ulauncher 5 (extension API v2).

## Installation

1. Open Ulauncher preferences → **Extensions** → **Add extension**.
2. Paste `https://github.com/rkulik/ulauncher-pinyin-tones`.

The default keyword is `pyt` and can be changed in the extension's preferences.

## Usage

Type the keyword followed by pinyin, with a tone number (`1`–`4`) after each syllable. Syllables can be separated by spaces or written together.

| Input        | Output | Note                                                                               |
| ------------ | ------ | ---------------------------------------------------------------------------------- |
| `ma1`        | `mā`   | first tone                                                                         |
| `ma2`        | `má`   | second tone                                                                        |
| `ma3`        | `mǎ`   | third tone                                                                         |
| `ma4`        | `mà`   | fourth tone                                                                        |
| `ma` / `ma5` | `ma`   | neutral tone: leave the number out, or use `5`/`0` when writing syllables together |
| `lv4`        | `lǜ`   | `v` is converted to `ü`                                                            |

The tone mark is placed according to the standard pinyin rules: on `a` or `e` if present, on the `o` in `ou`, otherwise on the last vowel (`xiu1` → `xiū`, `gui4` → `guì`). Text without tone numbers is left unchanged.

## License

Distributed under the [MIT License](https://github.com/rkulik/ulauncher-pinyin-tones/blob/main/LICENSE), Copyright © 2026-PRESENT [René Kulik](https://www.kulik.io/)
