[
{ "tag": "enum", "ns": 0, "name": "_Itable_IndexTypes", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:27:14", "fields": [{ "tag": "field", "name": "IUPTABLE_POINTERINDEXED", "value": 10 }, { "tag": "field", "name": "IUPTABLE_STRINGINDEXED", "value": 11 }] },
{ "tag": "typedef", "ns": 0, "name": "Itable_IndexTypes", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:31:3", "type": { "tag": ":enum", "name": "_Itable_IndexTypes", "id": 0 } },
{ "tag": "enum", "ns": 0, "name": "_Itable_Types", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:35:14", "fields": [{ "tag": "field", "name": "IUPTABLE_POINTER", "value": 0 }, { "tag": "field", "name": "IUPTABLE_STRING", "value": 1 }, { "tag": "field", "name": "IUPTABLE_FUNCPOINTER", "value": 2 }] },
{ "tag": "typedef", "ns": 0, "name": "Itable_Types", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:40:3", "type": { "tag": ":enum", "name": "_Itable_Types", "id": 0 } },
{ "tag": "typedef", "ns": 0, "name": "Ifunc", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:43:16", "type": { "tag": ":function-pointer" } },
{ "tag": "struct", "ns": 0, "name": "_Itable", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:45:8", "bit-size": 0, "bit-alignment": 0, "fields": [] },
{ "tag": "typedef", "ns": 0, "name": "Itable", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:46:24", "type": { "tag": "struct", "ns": 0, "name": "_Itable", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:45:8", "bit-size": 0, "bit-alignment": 0, "fields": [] } },
{ "tag": "function", "name": "iupTableCreate", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:52:9", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "indexType", "type": { "tag": "Itable_IndexTypes" } }], "return-type": { "tag": ":pointer", "type": { "tag": "Itable" } } },
{ "tag": "function", "name": "iupTableCreateSized", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:61:9", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "indexType", "type": { "tag": "Itable_IndexTypes" } }, { "tag": "parameter", "name": "initialSizeIndex", "type": { "tag": ":unsigned-int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":pointer", "type": { "tag": "Itable" } } },
{ "tag": "function", "name": "iupTableDestroy", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:66:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupTableClear", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:71:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupTableCount", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:75:5", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "function", "name": "iupTableSet", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:79:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "key", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "value", "type": { "tag": ":pointer", "type": { "tag": ":void" } } }, { "tag": "parameter", "name": "itemType", "type": { "tag": "Itable_Types" } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupTableSetFunc", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:84:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "key", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "func", "type": { "tag": "Ifunc" } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupTableGet", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:89:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "key", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":void" } } },
{ "tag": "function", "name": "iupTableGetFunc", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:95:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "key", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "value", "type": { "tag": ":pointer", "type": { "tag": ":pointer", "type": { "tag": ":void" } } } }], "return-type": { "tag": "Ifunc" } },
{ "tag": "function", "name": "iupTableGetTyped", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:99:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "key", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "itemType", "type": { "tag": ":pointer", "type": { "tag": "Itable_Types" } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":void" } } },
{ "tag": "function", "name": "iupTableRemove", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:105:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "key", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupTableFirst", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:116:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } },
{ "tag": "function", "name": "iupTableNext", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:120:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } },
{ "tag": "function", "name": "iupTableGetCurr", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:130:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":void" } } },
{ "tag": "function", "name": "iupTableGetCurrType", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:136:5", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "function", "name": "iupTableSetCurr", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:140:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "parameter", "name": "value", "type": { "tag": ":pointer", "type": { "tag": ":void" } } }, { "tag": "parameter", "name": "itemType", "type": { "tag": "Itable_Types" } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupTableRemoveCurr", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:145:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "it", "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } },
{ "tag": "enum", "ns": 0, "name": "_InativeType", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:24:14", "fields": [{ "tag": "field", "name": "IUP_TYPEVOID", "value": 0 }, { "tag": "field", "name": "IUP_TYPECONTROL", "value": 1 }, { "tag": "field", "name": "IUP_TYPECANVAS", "value": 2 }, { "tag": "field", "name": "IUP_TYPEDIALOG", "value": 3 }, { "tag": "field", "name": "IUP_TYPEIMAGE", "value": 4 }, { "tag": "field", "name": "IUP_TYPEMENU", "value": 5 }] },
{ "tag": "typedef", "ns": 0, "name": "InativeType", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:31:3", "type": { "tag": ":enum", "name": "_InativeType", "id": 0 } },
{ "tag": "enum", "ns": 0, "name": "_IchildType", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:35:14", "fields": [{ "tag": "field", "name": "IUP_CHILDNONE", "value": 0 }, { "tag": "field", "name": "IUP_CHILDMANY", "value": 1 }] },
{ "tag": "typedef", "ns": 0, "name": "IchildType", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:39:3", "type": { "tag": ":enum", "name": "_IchildType", "id": 0 } },
{ "tag": "struct", "ns": 0, "name": "Iclass_", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:41:16", "bit-size": 0, "bit-alignment": 0, "fields": [] },
{ "tag": "typedef", "ns": 0, "name": "Iclass", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:41:24", "type": { "tag": "struct", "ns": 0, "name": "Iclass_", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:41:16", "bit-size": 0, "bit-alignment": 0, "fields": [] } },
{ "tag": "struct", "ns": 0, "name": "Iclass_", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:45:8", "bit-size": 704, "bit-alignment": 32, "fields": [{ "tag": "field", "name": "name", "bit-offset": 0, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "field", "name": "format", "bit-offset": 32, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "field", "name": "nativetype", "bit-offset": 64, "bit-size": 32, "bit-alignment": 32, "type": { "tag": "InativeType" } }, { "tag": "field", "name": "childtype", "bit-offset": 96, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "is_interactive", "bit-offset": 128, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "has_attrib_id", "bit-offset": 160, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }, { "tag": "field", "name": "parent", "bit-offset": 192, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "field", "name": "attrib_func", "bit-offset": 224, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":pointer", "type": { "tag": "Itable" } } }, { "tag": "field", "name": "New", "bit-offset": 256, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "Release", "bit-offset": 288, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "Create", "bit-offset": 320, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "Map", "bit-offset": 352, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "UnMap", "bit-offset": 384, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "Destroy", "bit-offset": 416, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "GetInnerNativeContainerHandle", "bit-offset": 448, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "ChildAdded", "bit-offset": 480, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "ChildRemoved", "bit-offset": 512, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "LayoutUpdate", "bit-offset": 544, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "ComputeNaturalSize", "bit-offset": 576, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "SetChildrenCurrentSize", "bit-offset": 608, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "SetChildrenPosition", "bit-offset": 640, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }, { "tag": "field", "name": "DlgPopup", "bit-offset": 672, "bit-size": 32, "bit-alignment": 32, "type": { "tag": ":function-pointer" } }] },
{ "tag": "function", "name": "iupClassNew", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:196:9", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic_parent", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }], "return-type": { "tag": ":pointer", "type": { "tag": "Iclass" } } },
{ "tag": "function", "name": "iupClassRelease", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:202:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassMatch", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:207:5", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "classname", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "typedef", "ns": 0, "name": "IattribGetFunc", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:213:17", "type": { "tag": ":function-pointer" } },
{ "tag": "typedef", "ns": 0, "name": "IattribGetIdFunc", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:222:17", "type": { "tag": ":function-pointer" } },
{ "tag": "typedef", "ns": 0, "name": "IattribGetId2Func", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:231:17", "type": { "tag": ":function-pointer" } },
{ "tag": "typedef", "ns": 0, "name": "IattribSetFunc", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:239:15", "type": { "tag": ":function-pointer" } },
{ "tag": "typedef", "ns": 0, "name": "IattribSetIdFunc", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:248:15", "type": { "tag": ":function-pointer" } },
{ "tag": "typedef", "ns": 0, "name": "IattribSetId2Func", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:257:15", "type": { "tag": ":function-pointer" } },
{ "tag": "enum", "ns": 0, "name": "_IattribFlags", "id": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:262:14", "fields": [{ "tag": "field", "name": "IUPAF_DEFAULT", "value": 0 }, { "tag": "field", "name": "IUPAF_NO_INHERIT", "value": 1 }, { "tag": "field", "name": "IUPAF_NO_DEFAULTVALUE", "value": 2 }, { "tag": "field", "name": "IUPAF_NO_STRING", "value": 4 }, { "tag": "field", "name": "IUPAF_NOT_MAPPED", "value": 8 }, { "tag": "field", "name": "IUPAF_HAS_ID", "value": 16 }, { "tag": "field", "name": "IUPAF_READONLY", "value": 32 }, { "tag": "field", "name": "IUPAF_WRITEONLY", "value": 64 }, { "tag": "field", "name": "IUPAF_HAS_ID2", "value": 128 }, { "tag": "field", "name": "IUPAF_CALLBACK", "value": 256 }, { "tag": "field", "name": "IUPAF_NO_SAVE", "value": 512 }, { "tag": "field", "name": "IUPAF_NOT_SUPPORTED", "value": 1024 }, { "tag": "field", "name": "IUPAF_IHANDLENAME", "value": 2048 }, { "tag": "field", "name": "IUPAF_IHANDLE", "value": 4096 }] },
{ "tag": "typedef", "ns": 0, "name": "IattribFlags", "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:277:3", "type": { "tag": ":enum", "name": "_IattribFlags", "id": 0 } },
{ "tag": "function", "name": "iupClassRegisterAttribute", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:291:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "get", "type": { "tag": "IattribGetFunc" } }, { "tag": "parameter", "name": "set", "type": { "tag": "IattribSetFunc" } }, { "tag": "parameter", "name": "default_value", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "system_default", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "flags", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterAttributeId", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:300:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "get", "type": { "tag": "IattribGetIdFunc" } }, { "tag": "parameter", "name": "set", "type": { "tag": "IattribSetIdFunc" } }, { "tag": "parameter", "name": "flags", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterAttributeId2", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:307:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "get", "type": { "tag": "IattribGetId2Func" } }, { "tag": "parameter", "name": "set", "type": { "tag": "IattribSetId2Func" } }, { "tag": "parameter", "name": "flags", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterGetAttribute", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:314:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "get", "type": { "tag": ":pointer", "type": { "tag": "IattribGetFunc" } } }, { "tag": "parameter", "name": "set", "type": { "tag": ":pointer", "type": { "tag": "IattribSetFunc" } } }, { "tag": "parameter", "name": "default_value", "type": { "tag": ":pointer", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } } }, { "tag": "parameter", "name": "system_default", "type": { "tag": ":pointer", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } } }, { "tag": "parameter", "name": "flags", "type": { "tag": ":pointer", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterReplaceAttribFunc", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:323:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "_get", "type": { "tag": "IattribGetFunc" } }, { "tag": "parameter", "name": "_set", "type": { "tag": "IattribSetFunc" } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterReplaceAttribDef", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:327:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "_default_value", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "_system_default", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterReplaceAttribFlags", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:331:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "_flags", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassRegisterCallback", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:352:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "format", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassCallbackGetFormat", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:357:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } },
{ "tag": "function", "name": "iupClassObjectCurAttribIsInherit", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:454:7", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "function", "name": "iupClassUpdate", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:460:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassAttribIsRegistered", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:463:5", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "function", "name": "iupClassGetAttribNameInfo", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:464:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }, { "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "def_value", "type": { "tag": ":pointer", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } } }, { "tag": "parameter", "name": "flags", "type": { "tag": ":pointer", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupClassIsGlobalDefault", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:467:5", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }, { "tag": "parameter", "name": "colors", "type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } }], "return-type": { "tag": ":int", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "function", "name": "iupRegisterFindClass", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:25:9", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "name", "type": { "tag": ":pointer", "type": { "tag": ":char", "bit-size": 8, "bit-alignment": 8 } } }], "return-type": { "tag": ":pointer", "type": { "tag": "Iclass" } } },
{ "tag": "function", "name": "iupRegisterClass", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:29:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [{ "tag": "parameter", "name": "ic", "type": { "tag": ":pointer", "type": { "tag": "Iclass" } } }], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupRegisterInternalClasses", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:33:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupRegisterUpdateClasses", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:36:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupRegisterInit", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:40:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [], "return-type": { "tag": ":void" } },
{ "tag": "function", "name": "iupRegisterFinish", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:41:6", "variadic": false, "inline": false, "storage-class": "none", "parameters": [], "return-type": { "tag": ":void" } },
{ "tag": "const", "name": "__IUP_REGISTER_H", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_register.h:8:9", "type": { "tag": ":long", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "const", "name": "IUPAF_SAMEASSYSTEM", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:279:9", "type": { "tag": ":long", "bit-size": 32, "bit-alignment": 32 }, "value": -1 },
{ "tag": "const", "name": "__IUP_CLASS_H", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_class.h:8:9", "type": { "tag": ":long", "bit-size": 32, "bit-alignment": 32 } },
{ "tag": "const", "name": "__IUP_TABLE_H", "ns": 0, "location": "/home/mkennedy/.roswell/local-projects/lispnik/iup/classesdb/include/iup_table.h:9:9", "type": { "tag": ":long", "bit-size": 32, "bit-alignment": 32 } }
]
