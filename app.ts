import {
  renderJavaScriptVisitor,
  renderRustVisitor,
  renderPythonVisitor,
} from "@codama/renderers";
import { createFromRoot, updateProgramsVisitor } from "codama";
import { AnchorIdl, rootNodeFromAnchor } from "@codama/nodes-from-anchor";

function GenIdl(file: String, dirPath: String) {
  let anchorIdl = require(file);
  const rootNode = rootNodeFromAnchor(anchorIdl as AnchorIdl);
  const codama = createFromRoot(rootNode);
  codama.accept(renderPythonVisitor(dirPath));
}

GenIdl("./idls/pump.json", "pump");
GenIdl("./idls/idl-0.1.2.json", "Lifinity");
GenIdl("./idls/drift.json", "Drift");
