import { FindingTable } from "../components/FindingTable";
import type { Finding } from "../types/scanner";

const mockFindings: Finding[] = [
  {
    id: "PI-001",
    severity: "High",
    probeName: "Direct prompt injection behavior override",
    owaspCategory: "LLM01 Prompt Injection",
    evidence: "Demo placeholder evidence will appear here after scanner runs.",
    recommendation: "Add input filtering and stronger policy enforcement.",
  },
  {
    id: "LEAK-001",
    severity: "Critical",
    probeName: "Synthetic secret leakage",
    owaspCategory: "LLM02 Sensitive Information Disclosure",
    evidence: "Demo placeholder evidence will appear here after scanner runs.",
    recommendation: "Add output redaction and remove secrets from documents.",
  },
];

export function Findings() {
  return (
    <div className="space-y-6">
      <section>
        <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
          Findings
        </p>
        <h2 className="mt-3 text-3xl font-bold text-white">
          Security Findings
        </h2>
        <p className="mt-3 text-slate-400">
          Scanner findings will appear here after the backend scanner engine is
          implemented.
        </p>
      </section>

      <FindingTable findings={mockFindings} />
    </div>
  );
}