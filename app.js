/**
 * App.js - Módulo de interação da Régua de Governança
 * Integra com src/conde_governante para cálculos
 */

// Importar do módulo conde_governante se disponível
// import { calcularTriangulo, classificarGovernanca } from './src/conde_governante.js';

/**
 * Calcula as métricas de governança baseado nos valores de entrada
 * @param {number} etica - Valor de ética (0-1)
 * @param {number} eficiencia - Valor de eficiência (0-1)
 * @param {number} transparencia - Valor de transparência (0-1)
 * @returns {object} Objeto com cálculos e classificação
 */
export function calcularGovernanca(etica, eficiencia, transparencia) {
    // Validar valores
    const values = {
        etica: Math.max(0, Math.min(1, etica)),
        eficiencia: Math.max(0, Math.min(1, eficiencia)),
        transparencia: Math.max(0, Math.min(1, transparencia))
    };

    // Calcular média ponderada
    const media = (values.etica + values.eficiencia + values.transparencia) / 3;
    
    // Calcular nota em escala 0-10
    const nota = media * 10;

    // Calcular score de cada pilar
    const scores = {
        etica: values.etica * 10,
        eficiencia: values.eficiencia * 10,
        transparencia: values.transparencia * 10
    };

    return {
        notas: scores,
        media: media,
        notaFinal: nota,
        classificacao: classificarNota(nota),
        valores: values
    };
}

/**
 * Classifica a nota final
 * @param {number} nota - Nota de 0-10
 * @returns {object} Classificação com texto e nível
 */
export function classificarNota(nota) {
    if (nota >= 8.5) {
        return { nivel: 'Excelente', codigo: 'excelente', cor: '#4caf50' };
    } else if (nota >= 7) {
        return { nivel: 'Muito Bom', codigo: 'muito-bom', cor: '#8bc34a' };
    } else if (nota >= 5) {
        return { nivel: 'Bom', codigo: 'bom', cor: '#ffc107' };
    } else if (nota >= 3) {
        return { nivel: 'Regular', codigo: 'regular', cor: '#ff9800' };
    } else {
        return { nivel: 'Insuficiente', codigo: 'insuficiente', cor: '#f44336' };
    }
}

/**
 * Desenha o Triângulo de Conde no canvas
 * @param {CanvasRenderingContext2D} ctx - Contexto do canvas
 * @param {number} width - Largura do canvas
 * @param {number} height - Altura do canvas
 * @param {object} valores - Valores de ética, eficiência e transparência
 * @param {string} corPrimaria - Cor primária (padrão: #d4af37)
 */
export function desenharTriangloConde(ctx, width, height, valores, corPrimaria = '#d4af37') {
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) * 0.35;

    // Limpar canvas
    ctx.clearRect(0, 0, width, height);

    // Calcular vértices do triângulo equilátero
    const top = {
        x: centerX,
        y: centerY - radius
    };
    const bottomLeft = {
        x: centerX - (radius * Math.sqrt(3) / 2),
        y: centerY + (radius / 2)
    };
    const bottomRight = {
        x: centerX + (radius * Math.sqrt(3) / 2),
        y: centerY + (radius / 2)
    };

    // Desenhar linhas de grade
    ctx.strokeStyle = `${corPrimaria}33`;
    ctx.lineWidth = 1;
    for (let i = 1; i < 3; i++) {
        const factor = i / 3;
        const p1 = interpolate(top, bottomLeft, factor);
        const p2 = interpolate(top, bottomRight, factor);
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
    }

    // Desenhar triângulo base
    ctx.strokeStyle = corPrimaria;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(top.x, top.y);
    ctx.lineTo(bottomLeft.x, bottomLeft.y);
    ctx.lineTo(bottomRight.x, bottomRight.y);
    ctx.closePath();
    ctx.stroke();

    // Desenhar labels
    ctx.fillStyle = corPrimaria;
    ctx.font = 'bold 14px Segoe UI';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('Ética', top.x, top.y - 25);
    ctx.fillText('Eficiência', bottomLeft.x - 35, bottomLeft.y + 25);
    ctx.fillText('Transparência', bottomRight.x + 35, bottomRight.y + 25);

    // Calcular e desenhar ponto baseado em coordenadas baricêntricas
    const etica = valores.etica || 0;
    const eficiencia = valores.eficiencia || 0;
    const transparencia = valores.transparencia || 0;

    const point = {
        x: (etica * top.x + eficiencia * bottomLeft.x + transparencia * bottomRight.x),
        y: (etica * top.y + eficiencia * bottomLeft.y + transparencia * bottomRight.y)
    };

    // Desenhar aura ao redor do ponto
    const intensity = (etica + eficiencia + transparencia) / 3;
    ctx.fillStyle = `${corPrimaria}${Math.round(intensity * 100).toString(16).padStart(2, '0')}`;
    ctx.beginPath();
    ctx.arc(point.x, point.y, 20, 0, Math.PI * 2);
    ctx.fill();

    // Desenhar ponto central
    ctx.fillStyle = corPrimaria;
    ctx.beginPath();
    ctx.arc(point.x, point.y, 8, 0, Math.PI * 2);
    ctx.fill();

    // Desenhar círculo ao redor
    ctx.strokeStyle = corPrimaria;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(point.x, point.y, 15, 0, Math.PI * 2);
    ctx.stroke();
}

/**
 * Função auxiliar para interpolar entre dois pontos
 * @param {object} p1 - Ponto inicial
 * @param {object} p2 - Ponto final
 * @param {number} factor - Fator de interpolação (0-1)
 * @returns {object} Ponto interpolado
 */
function interpolate(p1, p2, factor) {
    return {
        x: p1.x + (p2.x - p1.x) * factor,
        y: p1.y + (p2.y - p1.y) * factor
    };
}

/**
 * Exportar todas as funções
 */
export default {
    calcularGovernanca,
    classificarNota,
    desenharTriangloConde
};
