import type { Severity } from "../types/scanner";

const severityClasses: Record<Severity, string> = {
  Critical: "bg-red-500/15 text-red-300 border-red-500/30",
  High: "bg-orange-500/15 text-orange-300 border-orange-500/30",
  Medium: "bg-yellow-500/15 text-yellow-300 border-yellow-500/30",
  Low: "bg-blue-500/15 text-blue-300 border-blue-500/30",
  Info: "bg-slate-500/15 text-slate-300 border-slate-500/30",
};

type SeverityBadgeProps = {
  severity: Severity;
};

export function SeverityBadge({ severity }: SeverityBadgeProps) {
  return (
    <span
      className={`inline-flex rounded-full border px-3 py-1 text-xs font-semibold ${severityClasses[severity]}`}
    >
      {severity}
    </span>
  );
}