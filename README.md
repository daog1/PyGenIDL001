# pygenidl001

The data structure is primarily based on AnchorPy, with function naming and functionality consistent with AnchorPy. It already supports basic types, enums, and complex types like structs. All functionalities are implemented, with future modifications to be made as needed. This is an example generated using the Pump IDL (https://github.com/daog1/PyGenIDL001). The specific code can be viewed in my branch (https://github.com/daog1/codama/commits/renderers-py).

The IDL file originates from solana-idl-lib.

The project added a notebooks directory, using .ipynb files to create tests for contract parsing instructions, building instructions, and retrieving account information. It includes pump.ipynb and jup.ipynb. Now, complex contract definitions like jup can be parsed and built, and other contracts are not an issue in this regard. If you have any modifications or suggestions, please raise them as issues.


```
function GenIdl(file: String, dirPath: String) {
  let anchorIdl = require(file);
  const rootNode = rootNodeFromAnchor(anchorIdl as AnchorIdl);
  const codama = createFromRoot(rootNode);
  codama.accept(renderPythonVisitor(dirPath));
}

GenIdl("./idls/pump.json", "pump");
GenIdl("./idls/idl-0.1.2.json", "Lifinity");
```
