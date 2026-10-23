using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;

namespace GkcExtract
{
    public sealed class AttrInfo
    {
        public string Name { get; set; }
        public string Text { get; set; }
    }

    public sealed class ParamInfo
    {
        public string Type { get; set; }
        public string Name { get; set; }
        public string Default { get; set; }
        public string Modifier { get; set; }
    }

    public sealed class FieldInfo
    {
        public string Name { get; set; }
        public string Type { get; set; }
        public string Modifiers { get; set; }
        public string Init { get; set; }
        public List<AttrInfo> Attributes { get; set; } = new();
        public string Doc { get; set; }
        public int Line { get; set; }
        public bool IsStatic { get; set; }
        public bool IsConst { get; set; }
        public bool IsReadOnly { get; set; }
        public string Comment { get; set; }
    }

    public sealed class PropertyInfo
    {
        public string Name { get; set; }
        public string Type { get; set; }
        public string Modifiers { get; set; }
        public string Accessors { get; set; }
        public List<AttrInfo> Attributes { get; set; } = new();
        public string Doc { get; set; }
        public int Line { get; set; }
        public bool IsStatic { get; set; }
    }

    public sealed class MethodInfo
    {
        public string Name { get; set; }
        public string ReturnType { get; set; }
        public string Modifiers { get; set; }
        public List<ParamInfo> Params { get; set; } = new();
        public List<AttrInfo> Attributes { get; set; } = new();
        public string Doc { get; set; }
        public int Line { get; set; }
        public bool IsStatic { get; set; }
        public bool IsOverride { get; set; }
        public bool IsVirtual { get; set; }
        public bool IsAbstract { get; set; }
        public bool IsGeneric { get; set; }
        public string Signature { get; set; }
    }

    public sealed class EventInfo
    {
        public string Name { get; set; }
        public string Type { get; set; }
        public string Modifiers { get; set; }
        public string Doc { get; set; }
        public int Line { get; set; }
    }

    public sealed class EnumMemberInfo
    {
        public string Name { get; set; }
        public string Value { get; set; }
        public string Doc { get; set; }
    }

    public sealed class TypeInfo
    {
        public string Namespace { get; set; } = "";
        public string Name { get; set; }
        public string Kind { get; set; }
        public string Modifiers { get; set; }
        public List<string> BaseTypes { get; set; } = new();
        public string File { get; set; }
        public int Line { get; set; }
        public bool IsEditor { get; set; }
        public bool IsNested { get; set; }
        public string ContainingType { get; set; }
        public List<AttrInfo> Attributes { get; set; } = new();
        public string Doc { get; set; }
        public string Comment { get; set; }
        public List<FieldInfo> Fields { get; set; } = new();
        public List<PropertyInfo> Properties { get; set; } = new();
        public List<MethodInfo> Methods { get; set; } = new();
        public List<EventInfo> Events { get; set; } = new();
        public List<EnumMemberInfo> EnumMembers { get; set; } = new();
    }

    public static class Program
    {
        static readonly string[] Symbols =
        {
            "UNITY_EDITOR", "UNITY_5_3_OR_NEWER", "UNITY_2017_1_OR_NEWER", "UNITY_2018_1_OR_NEWER",
            "UNITY_2019_1_OR_NEWER", "UNITY_2020_1_OR_NEWER", "UNITY_2021_1_OR_NEWER",
            "UNITY_2022_1_OR_NEWER", "UNITY_6000_0_OR_NEWER",
            "ENABLE_INPUT_SYSTEM", "ENABLE_LEGACY_INPUT_MANAGER",
            "GKC_INPUT_SYSTEM_ENABLED"
        };

        public static int Main(string[] args)
        {
            var root = args.Length > 0 ? args[0] : @"D:\dev\Unity\GKC AI\Assets\Game Kit Controller\Scripts";
            var output = args.Length > 1 ? args[1] : @"D:\dev\gkc_ref\build\types.json";

            var files = Directory.GetFiles(root, "*.cs", SearchOption.AllDirectories)
                                 .OrderBy(f => f, StringComparer.Ordinal)
                                 .ToArray();

            var options = new CSharpParseOptions(LanguageVersion.Latest, preprocessorSymbols: Symbols);
            var types = new List<TypeInfo>();

            foreach (var file in files)
            {
                var text = File.ReadAllText(file);
                var tree = CSharpSyntaxTree.ParseText(text, options, path: file);
                var rootNode = tree.GetRoot();
                var rel = Path.GetRelativePath(root, file).Replace('\\', '/');
                var isEditor = rel.StartsWith("Editor/", StringComparison.OrdinalIgnoreCase);

                foreach (var t in rootNode.DescendantNodes().OfType<BaseTypeDeclarationSyntax>())
                {
                    var info = ExtractType(t, rel, isEditor);
                    if (info != null) types.Add(info);
                }
            }

            Directory.CreateDirectory(Path.GetDirectoryName(output)!);
            var jsonOptions = new JsonSerializerOptions { WriteIndented = false };
            File.WriteAllText(output, JsonSerializer.Serialize(types, jsonOptions), new UTF8Encoding(false));

            Console.WriteLine($"files={files.Length} types={types.Count}");
            return 0;
        }

        static TypeInfo ExtractType(BaseTypeDeclarationSyntax node, string file, bool isEditor)
        {
            var info = new TypeInfo
            {
                Name = node.Identifier.ValueText,
                Kind = node switch
                {
                    ClassDeclarationSyntax => "class",
                    StructDeclarationSyntax => "struct",
                    InterfaceDeclarationSyntax => "interface",
                    EnumDeclarationSyntax => "enum",
                    RecordDeclarationSyntax => "record",
                    _ => "type"
                },
                Modifiers = Mods(node.Modifiers),
                File = file,
                Line = node.GetLocation().GetLineSpan().StartLinePosition.Line + 1,
                IsEditor = isEditor,
                IsNested = node.Parent is TypeDeclarationSyntax,
                ContainingType = (node.Parent as TypeDeclarationSyntax)?.Identifier.ValueText,
                Namespace = NamespaceOf(node),
                Doc = DocOf(node),
                Comment = TrailingComment(node)
            };

            info.Attributes = Attrs(node.AttributeLists);

            if (node is TypeDeclarationSyntax tds && tds.BaseList != null)
                info.BaseTypes = tds.BaseList.Types.Select(x => Norm(x.Type.ToString())).ToList();

            if (node is EnumDeclarationSyntax enumDecl)
            {
                foreach (var mem in enumDecl.Members)
                {
                    info.EnumMembers.Add(new EnumMemberInfo
                    {
                        Name = mem.Identifier.ValueText,
                        Value = mem.EqualsValue?.Value.ToString(),
                        Doc = DocOf(mem)
                    });
                }
                return info;
            }

            foreach (var member in ((TypeDeclarationSyntax)node).Members)
            {
                switch (member)
                {
                    case FieldDeclarationSyntax f:
                        {
                            var type = Norm(f.Declaration.Type.ToString());
                            foreach (var v in f.Declaration.Variables)
                            {
                                info.Fields.Add(new FieldInfo
                                {
                                    Name = v.Identifier.ValueText,
                                    Type = type,
                                    Modifiers = Mods(f.Modifiers),
                                    Init = v.Initializer?.Value.ToString(),
                                    Attributes = Attrs(f.AttributeLists),
                                    Doc = DocOf(f),
                                    Line = v.GetLocation().GetLineSpan().StartLinePosition.Line + 1,
                                    IsStatic = f.Modifiers.Any(SyntaxKind.StaticKeyword),
                                    IsConst = f.Modifiers.Any(SyntaxKind.ConstKeyword),
                                    IsReadOnly = f.Modifiers.Any(SyntaxKind.ReadOnlyKeyword),
                                    Comment = TrailingComment(f)
                                });
                            }
                            break;
                        }
                    case EventFieldDeclarationSyntax e:
                        {
                            var type = Norm(e.Declaration.Type.ToString());
                            foreach (var v in e.Declaration.Variables)
                            {
                                info.Events.Add(new EventInfo
                                {
                                    Name = v.Identifier.ValueText,
                                    Type = type,
                                    Modifiers = Mods(e.Modifiers),
                                    Doc = DocOf(e),
                                    Line = v.GetLocation().GetLineSpan().StartLinePosition.Line + 1
                                });
                            }
                            break;
                        }
                    case PropertyDeclarationSyntax p:
                        {
                            info.Properties.Add(new PropertyInfo
                            {
                                Name = p.Identifier.ValueText,
                                Type = Norm(p.Type.ToString()),
                                Modifiers = Mods(p.Modifiers),
                                Accessors = string.Join("/", p.AccessorList?.Accessors.Select(a => a.Keyword.ValueText) ?? Enumerable.Empty<string>()),
                                Attributes = Attrs(p.AttributeLists),
                                Doc = DocOf(p),
                                Line = p.GetLocation().GetLineSpan().StartLinePosition.Line + 1,
                                IsStatic = p.Modifiers.Any(SyntaxKind.StaticKeyword)
                            });
                            break;
                        }
                    case MethodDeclarationSyntax m:
                        {
                            var ps = m.ParameterList.Parameters.Select(x => new ParamInfo
                            {
                                Type = Norm(x.Type?.ToString() ?? ""),
                                Name = x.Identifier.ValueText,
                                Default = x.Default?.Value.ToString(),
                                Modifier = string.Join(" ", x.Modifiers.Select(z => z.ValueText))
                            }).ToList();

                            info.Methods.Add(new MethodInfo
                            {
                                Name = m.Identifier.ValueText,
                                ReturnType = Norm(m.ReturnType.ToString()),
                                Modifiers = Mods(m.Modifiers),
                                Params = ps,
                                Attributes = Attrs(m.AttributeLists),
                                Doc = DocOf(m),
                                Line = m.GetLocation().GetLineSpan().StartLinePosition.Line + 1,
                                IsStatic = m.Modifiers.Any(SyntaxKind.StaticKeyword),
                                IsOverride = m.Modifiers.Any(SyntaxKind.OverrideKeyword),
                                IsVirtual = m.Modifiers.Any(SyntaxKind.VirtualKeyword),
                                IsAbstract = m.Modifiers.Any(SyntaxKind.AbstractKeyword),
                                IsGeneric = m.TypeParameterList != null,
                                Signature = BuildSignature(m, ps)
                            });
                            break;
                        }
                    case ConstructorDeclarationSyntax _:
                    case DelegateDeclarationSyntax _:
                        break;
                }
            }

            return info;
        }

        static string BuildSignature(MethodDeclarationSyntax m, List<ParamInfo> ps)
        {
            var generic = m.TypeParameterList?.ToString() ?? "";
            var args = string.Join(", ", ps.Select(p =>
                (string.IsNullOrEmpty(p.Modifier) ? "" : p.Modifier + " ") + p.Type + " " + p.Name +
                (string.IsNullOrEmpty(p.Default) ? "" : " = " + p.Default)));
            return $"{m.Identifier.ValueText}{generic}({args})";
        }

        static string NamespaceOf(SyntaxNode node)
        {
            var parts = new List<string>();
            for (var n = node.Parent; n != null; n = n.Parent)
                if (n is NamespaceDeclarationSyntax ns) parts.Insert(0, ns.Name.ToString());
                else if (n is FileScopedNamespaceDeclarationSyntax fns) parts.Insert(0, fns.Name.ToString());
            return string.Join(".", parts);
        }

        static List<AttrInfo> Attrs(SyntaxList<AttributeListSyntax> lists)
        {
            var result = new List<AttrInfo>();
            foreach (var list in lists)
                foreach (var a in list.Attributes)
                {
                    var text = a.ToString();
                    var name = a.Name.ToString();
                    if (name.EndsWith("Attribute")) name = name[..^9];
                    if (name.Contains('.')) name = name[(name.LastIndexOf('.') + 1)..];
                    result.Add(new AttrInfo { Name = name, Text = Collapse(text) });
                }
            return result;
        }

        static string DocOf(SyntaxNode node)
        {
            var text = string.Join("\n", node.GetLeadingTrivia()
                .Where(t => t.IsKind(SyntaxKind.SingleLineDocumentationCommentTrivia) ||
                            t.IsKind(SyntaxKind.MultiLineDocumentationCommentTrivia))
                .Select(t => t.ToFullString()));

            if (string.IsNullOrWhiteSpace(text)) return null;

            var cleaned = new StringBuilder();
            foreach (var raw in text.Split('\n'))
            {
                var line = raw.Trim();
                if (line.StartsWith("///")) line = line[3..];
                else if (line.StartsWith("/**")) line = line[3..];
                else if (line.StartsWith("*/")) continue;
                else if (line.StartsWith("*")) line = line[1..];
                line = line.Trim();
                if (line.StartsWith("<summary>")) line = line[9..];
                if (line.EndsWith("</summary>")) line = line[..^10];
                if (line.StartsWith("</")) continue;
                line = System.Text.RegularExpressions.Regex.Replace(line, "<[^>]+>", "").Trim();
                if (line.Length > 0) cleaned.AppendLine(line);
            }
            var result = cleaned.ToString().Trim();
            return result.Length == 0 ? null : result;
        }

        static string TrailingComment(SyntaxNode node)
        {
            var triviaList = node.GetLastToken().TrailingTrivia
                .Concat(node.GetTrailingTrivia())
                .ToList();

            var trivia = triviaList.FirstOrDefault(t =>
                t.IsKind(SyntaxKind.SingleLineCommentTrivia) ||
                t.IsKind(SyntaxKind.MultiLineCommentTrivia));

            if (trivia == default) return null;
            var t = trivia.ToFullString().Trim();
            if (t.StartsWith("//")) t = t[2..].Trim();
            else if (t.StartsWith("/*")) t = t[2..].Trim();
            if (t.EndsWith("*/")) t = t[..^2].Trim();
            return t.Length == 0 ? null : t;
        }

        static string Mods(SyntaxTokenList tokens) =>
            string.Join(" ", tokens.Select(t => t.ValueText).Where(s => s.Length > 0));

        static string Collapse(string s) =>
            System.Text.RegularExpressions.Regex.Replace(s, @"\s+", " ").Trim();

        static string Norm(string s) =>
            System.Text.RegularExpressions.Regex.Replace(s, @"\s+", " ").Trim();
    }
}

