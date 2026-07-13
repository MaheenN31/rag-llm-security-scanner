import type { Finding } from "../types/scanner";
import { SeverityBadge } from "./SeverityBadge";

type FindingTableProps = {
  findings: Finding[];
};

export function FindingTable({ findings }: FindingTableProps) {
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900/70">
      <table className="w-full border-collapse text-left text-sm">
        <thead className="border-b border-slate-800 bg-slate-950/60 text-slate-400">
          <tr>
            <th className="px-5 py-4 font-medium">Severity</th>
            <th className="px-5 py-4 font-medium">Probe</th>
            <th className="px-5 py-4 font-medium">OWASP Category</th>
            <th className="px-5 py-4 font-medium">Recommendation</th>
          </tr>
        </thead>
        <tbody>
          {findings.map((finding) => (
            <tr key={finding.id} className="border-b border-slate-800/80">
              <td className="px-5 py-4">
                <SeverityBadge severity={finding.severity} />
              </td>
              <td className="px-5 py-4 text-white">{finding.probeName}</td>
              <td className="px-5 py-4 text-slate-300">
                {finding.owaspCategory}
              </td>
              <td className="px-5 py-4 text-slate-400">
                {finding.recommendation}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}