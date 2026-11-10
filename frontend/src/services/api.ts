// Support VITE_API_URL for Render backend or fallback to /api (Netlify proxy / local Vite)
const getApiBase = (): string => {
  const envUrl = (import.meta.env.VITE_API_URL as string | undefined)?.trim();
  if (!envUrl) return '/api';
  const clean = envUrl.replace(/\/$/, '');
  return clean.endsWith('/api') ? clean : `${clean}/api`;
};

const API_BASE = getApiBase();

/**
 * Validates and parses API responses.
 * Detects if Netlify or an intermediate proxy returned HTML (e.g. index.html SPA fallback)
 * and produces an explicit, actionable error message rather than JSON parse syntax errors.
 */
async function handleResponse<T>(res: Response, errorMsg: string): Promise<T> {
  const contentType = res.headers.get('content-type') || '';
  if (!res.ok) {
    let detail = '';
    try {
      if (contentType.includes('application/json')) {
        const errJson = await res.json();
        detail = errJson.detail || errJson.message || '';
      }
    } catch {
      // ignore
    }
    throw new Error(detail ? `${errorMsg}: ${detail}` : `${errorMsg} (HTTP ${res.status})`);
  }

  if (!contentType.includes('application/json')) {
    throw new Error(
      `Invalid response from API (${res.url}). Expected application/json but received ${contentType || 'HTML'}. ` +
      `Please ensure your Render backend is deployed and VITE_API_URL is configured in Netlify.`
    );
  }

  return res.json();
}

export interface OverviewData {
  matches_analyzed: number;
  deliveries_analyzed: number;
  mapped_players: number;
  coverage_period: string;
  high_pressure_deliveries: number;
  high_pressure_pct: number;
  extreme_pressure_pct: number;
  normal_leverage_pct: number;
  top_batters_preview: any[];
  top_bowlers_preview: any[];
  actionable_bowlers_preview: any[];
  simulated_purse_capacity_cr: number;
  total_purse_cr: number;
  overseas_slots_available: string;
  squad_slots: string;
}

export interface Batter {
  rank: number;
  player_id: number;
  player_name: string;
  team: string;
  batting_role: string;
  matches_analyzed: number;
  pressure_innings: number;
  pressure_balls_faced: number;
  pressure_runs_scored: number;
  pressure_batting_avg: number;
  pressure_strike_rate: number;
  death_strike_rate: number;
  chase_strike_rate: number;
  delta_strike_rate_vs_normal: number;
  bootstrap_95_ci_lower_sr: number;
  bootstrap_95_ci_upper_sr: number;
  bootstrap_standard_error_sr: number;
  bpri_score: number;
  sample_size_saturation_index_pct: number;
  uncertainty_interpretation: string;
  ipl_auction_eligibility: string;
}

export interface Bowler {
  rank: number;
  player_id: number;
  player_name: string;
  team: string;
  bowling_role: string;
  matches_analyzed: number;
  pressure_innings: number;
  pressure_overs_bowled: number;
  pressure_legal_balls: number;
  pressure_runs_conceded: number;
  pressure_wickets: number;
  pressure_bowling_avg: number;
  pressure_economy_rate: number;
  pressure_bowling_strike_rate: number;
  death_economy_rate: number;
  delta_economy_vs_normal: number;
  bootstrap_95_ci_lower_econ: number;
  bootstrap_95_ci_upper_econ: number;
  bootstrap_standard_error_econ: number;
  bowpri_score: number;
  sample_size_saturation_index_pct: number;
  uncertainty_interpretation: string;
  ipl_auction_eligibility: string;
}

export interface CompareResult {
  player_type: 'batter' | 'bowler';
  player_a: {
    player_id: number;
    name: string;
    team: string;
    score: number;
    ci: [number, number];
    sssi: number;
  };
  player_b: {
    player_id: number;
    name: string;
    team: string;
    score: number;
    ci: [number, number];
    sssi: number;
  };
  ci_overlap: boolean;
  uncertainty_note: string;
  radar_data: Array<{
    metric: string;
    player_a: number;
    player_b: number;
    val_a: number;
    val_b: number;
  }>;
  deltas: {
    score_delta: number;
    [key: string]: number;
  };
}

export const api = {
  async getOverview(): Promise<OverviewData> {
    const res = await fetch(`${API_BASE}/overview`);
    return handleResponse<OverviewData>(res, 'Failed to load overview data');
  },

  async getBatters(role?: string, search?: string, sortBy = 'bpri_score', ascending = false): Promise<Batter[]> {
    const params = new URLSearchParams();
    if (role) params.append('role', role);
    if (search) params.append('search', search);
    params.append('sort_by', sortBy);
    params.append('ascending', String(ascending));
    const res = await fetch(`${API_BASE}/players/batters?${params.toString()}`);
    return handleResponse<Batter[]>(res, 'Failed to load batters');
  },

  async getBowlers(actionableOnly = false, search?: string, sortBy = 'bowpri_score', ascending = false): Promise<Bowler[]> {
    const params = new URLSearchParams();
    params.append('actionable_only', String(actionableOnly));
    if (search) params.append('search', search);
    params.append('sort_by', sortBy);
    params.append('ascending', String(ascending));
    const res = await fetch(`${API_BASE}/players/bowlers?${params.toString()}`);
    return handleResponse<Bowler[]>(res, 'Failed to load bowlers');
  },

  async getPlayerProfile(playerId: number): Promise<any> {
    const res = await fetch(`${API_BASE}/players/${playerId}`);
    return handleResponse<any>(res, `Player ${playerId} not found`);
  },

  async comparePlayers(playerAId: number, playerBId: number, playerType: 'batter' | 'bowler'): Promise<CompareResult> {
    const res = await fetch(`${API_BASE}/compare?player_a_id=${playerAId}&player_b_id=${playerBId}&player_type=${playerType}`);
    return handleResponse<CompareResult>(res, 'Failed to compare players');
  },

  async getPressureSummary(): Promise<any> {
    const res = await fetch(`${API_BASE}/pressure/summary`);
    return handleResponse<any>(res, 'Failed to load pressure summary');
  },

  async getAuctionTargets(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/auction/targets`);
    return handleResponse<any[]>(res, 'Failed to load auction targets');
  },

  async simulateAuction(remainingPurse: number, bids: Record<string, number>): Promise<any> {
    const res = await fetch(`${API_BASE}/auction/simulate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ remaining_purse: remainingPurse, bids })
    });
    return handleResponse<any>(res, 'Failed to run auction simulation');
  },

  async getMethodology(): Promise<any> {
    const res = await fetch(`${API_BASE}/methodology`);
    return handleResponse<any>(res, 'Failed to load methodology');
  }
};
