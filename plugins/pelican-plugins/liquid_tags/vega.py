"""
Vega Tag
---------

"""
import re

import six

from .mdx_liquid_tags import LiquidTags

SYNTAX = '{% vega path/to/vega.json %}'

# Regular expression to match the entire syntax
ReVega = re.compile(
    r"([\S]+)\s([\S]+)"
)


@LiquidTags.register("vega")
def vega(preprocessor, tag, markup):

    # Parse the markup string
    match = ReVega.search(markup)
    if match:
        groups = match.groups()
        vega_path = groups[1]
        vega_obj = groups[0]
    else:
        raise ValueError(
            "Error processing input. " "Expected syntax: {0}".format(SYNTAX)
        )
    
    vega_var = vega_obj + "Var"

    tag_string = """<div id="cent"><div id="{vega_obj}" class="vis-container"></div></div>
                    <script>
                    var {vega_var}= "{vega_path}";
                    vegaEmbed('#{vega_obj}', {vega_var});
                    </script>""".format(
                        vega_var=vega_var, vega_obj=vega_obj, vega_path=vega_path
                    )

    return preprocessor.configs.htmlStash.store(tag_string)


# ----------------------------------------------------------------------
# This import allows image tag to be a Pelican plugin
from .liquid_tags import register  # noqa
