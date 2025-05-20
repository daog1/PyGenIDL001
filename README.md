# pygenidl001

The data structure is primarily based on AnchorPy, with function naming and functionality consistent with AnchorPy. Basic types have already been implemented, but enum types are not yet supported. This is an example generated using the Pump IDL (https://github.com/daog1/PyGenIDL001). The specific code can be viewed in my branch (https://github.com/daog1/codama/commits/renderers-py).


```
import {
  renderJavaScriptVisitor,
  renderRustVisitor,
  renderPythonVisitor,
} from "@codama/renderers";
import { createFromRoot, updateProgramsVisitor } from "codama";
import { AnchorIdl, rootNodeFromAnchor } from "@codama/nodes-from-anchor";
import anchorIdl from "./idls/pump.json";

const rootNode = rootNodeFromAnchor(anchorIdl as AnchorIdl);
const codama = createFromRoot(rootNode);
codama.accept(renderPythonVisitor("pump"));
```
