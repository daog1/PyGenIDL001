import {
  renderJavaScriptVisitor,
  renderRustVisitor,
  renderPythonVisitor,
} from "@codama/renderers";
import { createFromRoot, updateProgramsVisitor } from "codama";
import { AnchorIdl, rootNodeFromAnchor } from "@codama/nodes-from-anchor";
import { readJson } from "@codama/renderers-core";
import path from 'path';
import { rootNode } from "@codama/nodes";
//const path = require('node:path');

function GenIdl2(file: String, dirPath: String) {
  let anchorIdl = require(file);
  const rootNode = rootNodeFromAnchor(anchorIdl as AnchorIdl);
  const codama = createFromRoot(rootNode);
  codama.accept(renderPythonVisitor(dirPath));
}
function GenIdl(file: String, dirPath: String) {
  const idl = readJson(path.join(__dirname, file));

  let root;
  try {
    if (idl?.metadata?.spec) {
      root = rootNodeFromAnchor(idl);
    } else {
      root = rootNode(idl.program, idl.additionalPrograms);
    }
    //const rootNode = rootNodeFromAnchor( as AnchorIdl);
    const codama = createFromRoot(root);
    codama.accept(renderPythonVisitor(dirPath));
  }catch (e) {
   console.error(`${file}  `+e);
  }

}
function GenIdlJs(file: String, dirPath: String) {
  let anchorIdl = require(file);
  const rootNode = rootNodeFromAnchor(anchorIdl as AnchorIdl);
  const codama = createFromRoot(rootNode);
  codama.accept(renderJavaScriptVisitor(dirPath));
}


GenIdl("./idls/pump.json", "pump");
GenIdl2("./idls/idl-0.1.2.json", "Lifinity");
GenIdl2("./idls/drift.json", "Drift");
GenIdl("./idls/jup.json", "jup");
// GenIdl("./idls/scope.json", "scope");
GenIdl("./idls/dynamic_ix.json", "dynamic_ix");
GenIdl("./idls/dummy.json", "dummy");



GenIdl2("./idls/scope.json", "scope");
//GenIdl2("./idls/drift.json", "Drift");
//GenIdl("./idls/dummy.json", "dummy");
GenIdl("./idls/system.json", "system");
GenIdl2("./idls/klend.json", "klend");
// GenIdlJs("./idls/pump.json", "pumpjs");
// GenIdlJs("./idls/idl-0.1.2.json", "Lifinityjs");
// GenIdlJs("./idls/drift.json", "Driftjs");
// GenIdlJs("./idls/pump_amm.json", "pump_amm");
//GenIdl("./idls/pump_amm.json", "pump_amm");
//GenIdl("./idls/reward_pool.json", "reward_pool");

//GenIdl("./idls/okxrouter.json", "okxrouter");

//GenIdlJs("./idls/pump_amm.json", "pump_amm_js");
