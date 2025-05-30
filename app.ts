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
function GenIdlJs(file: String, dirPath: String) {
  let anchorIdl = require(file);
  const rootNode = rootNodeFromAnchor(anchorIdl as AnchorIdl);
  const codama = createFromRoot(rootNode);
  codama.accept(renderJavaScriptVisitor(dirPath));
}

GenIdl("./idls/pump.json", "pump");
GenIdl("./idls/idl-0.1.2.json", "Lifinity");
GenIdl("./idls/drift.json", "Drift");
GenIdl("./idls/jup.json", "jup");
// GenIdlJs("./idls/pump.json", "pumpjs");
// GenIdlJs("./idls/idl-0.1.2.json", "Lifinityjs");
// GenIdlJs("./idls/drift.json", "Driftjs");
// GenIdlJs("./idls/pump_amm.json", "pump_amm");
//GenIdl("./idls/pump_amm.json", "pump_amm");
//GenIdl("./idls/reward_pool.json", "reward_pool");

//GenIdl("./idls/okxrouter.json", "okxrouter");

//GenIdlJs("./idls/pump_amm.json", "pump_amm_js");
