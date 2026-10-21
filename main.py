from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from pinyin import convert_text

ICON = "images/icon.png"


class KeywordQueryEventListener(EventListener):
    def on_event(self, event: KeywordQueryEvent, extension: Extension) -> RenderResultListAction:
        argument = event.get_argument()
        if not argument:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=ICON,
                    name="Type pinyin with tone numbers",
                    description="e.g. ni3 hao3",
                    on_enter=DoNothingAction(),
                ),
            ])

        result = convert_text(argument)

        return RenderResultListAction([
            ExtensionResultItem(
                icon=ICON,
                name=result,
                description="Enter to copy",
                on_enter=CopyToClipboardAction(result),
            ),
        ])


class PinyinTonesExtension(Extension):
    def __init__(self) -> None:
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


if __name__ == "__main__":
    PinyinTonesExtension().run()
