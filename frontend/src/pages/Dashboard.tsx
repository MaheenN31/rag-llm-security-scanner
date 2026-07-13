import { useEffect, useState } from "react";
import { getHealth } from "../api/client";
import { StatCard } from "../components/StatCard";
import type { HealthResponse, ScanSummary } from "../types/scanner";

const mockSummary: ScanSummary = {
  totalProbes: 10,
  passed: 0,
  failed: 0,
  riskScore: 0,
  criticalFindings: 0,
};

export function Dashboard() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [apiError, setApiError] = useState<string | null>(null);

  useEffect(() => {
    getHealth()
      .then(setHealth)
      .catch((error: unknown) => {
        const message =
          error instanceof Error ? error.message : "Unable to reach backend";
        setApiError(message);
      });
  }, []);

  return (
    <div className="space-y-8">
      <section>
        <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
          Scan Overview
        </p>
        <h2 className="mt-3 text-4xl font-bold tracking-tight text-white">
          RAG / LLM Security Scanner
        </h2>
        <p className="mt-4 max-w-3xl text-slate-400">
          Monitor prompt injection, sensitive-data leakage, system-prompt
          exposure, unauthorized retrieval, and weak grounding risks from one
          dashboard.
        </p>
      </section>

      <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-5">
        <StatCard
          label="Total Probes"
          value={mockSummary.totalProbes}
          helper="MVP scanner target"
        />
        <StatCard label="Passed" value={mockSummary.passed} />
        <StatCard label="Failed" value={mockSummary.failed} />
        <StatCard label="Risk Score" value={`${mockSummary.riskScore}/100`} />
        <StatCard
          label="Critical Findings"
          value={mockSummary.criticalFindings}
        />
      </section>

      <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
        <h3 className="text-lg font-semibold text-white">Backend Status</h3>

        {health ? (
          <div className="mt-4 rounded-xl border border-emerald-500/20 bg-emerald-500/10 p-4 text-sm text-emerald-200">
            API connected successfully. App: <strong>{health.app_name}</strong>.
            Environment: <strong>{health.environment}</strong>.
          </div>
        ) : (
          <div className="mt-4 rounded-xl border border-yellow-500/20 bg-yellow-500/10 p-4 text-sm text-yellow-200">
            {apiError
              ? `Backend not reachable yet: ${apiError}`
              : "Checking backend connection..."}
          </div>
        )}
      </section>
    </div>
  );
}